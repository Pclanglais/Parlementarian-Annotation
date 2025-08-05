import os
import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

print(device)

from datasets import load_dataset
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
    BitsAndBytesConfig,
    HfArgumentParser,
    TrainingArguments,
    pipeline,
    logging,
    LlamaTokenizerFast
)
from peft import LoraConfig, PeftModel, get_peft_model
from trl import SFTTrainer, SFTConfig

# Le modèle que nous allons utiliser dans le Hugging Face hub
model_name = "Qwen/Qwen3-8B"

torch.cuda.empty_cache()

# Le nom du nouveau modèle
new_model_name = "./qwen-8b-debate"

# The output directory where the model predictions and checkpoints will be written
output_dir = "./qwen-8b-debate"

# Tensorboard logs
tb_log_dir = "./qwen-8b-debate/logs"

# Nombre de steps : à ajuster selon la taille du corpus et le nombre d'epochs à faire tourner.
#12000 => environ 3 epochs.
max_steps = 12000

# Les paramètres importants !!
per_device_train_batch_size = 1 #Nombre d'exemples envoyés par batch. En réalité juste un exemple par batch : efficace pour les plus petits sets pour diminuer l'overfitting.
learning_rate = 1e-4 #Taux d'apprentissage élevé => on change drastiquement la structure des instructions Qwen et Qwen 3 est un peu "overcooked"
max_seq_length = 16384 #C'est la fenêtre contextuelle. 16000 tokens est plutôt confortable.
save_steps = 3000 # Sauvegarde des steps, approximativement à chaque époque.
# Learning rate schedule. Je préfère linéaire à cosine => trop instable.
lr_scheduler_type = "linear"


#Les autres paramètres
local_rank = -1
per_device_eval_batch_size = 1
gradient_accumulation_steps = 1
max_grad_norm = 0.3
weight_decay = 0.01
lora_alpha = 16
lora_dropout = 0.1
lora_r = 64
# Group sequences into batches with same length (saves memory and speeds up training considerably)
group_by_length = True

# Activate 4-bit precision base model loading
use_4bit = True

# Activate nested quantization for 4-bit base models
use_nested_quant = False

# Compute dtype for 4-bit base models
bnb_4bit_compute_dtype = "float16"

# Quantization type (fp4 or nf4=
bnb_4bit_quant_type = "nf4"

# Number of training epochs
num_train_epochs = 1

# Enable fp16 training
fp16 = True

# Enable bf16 training
bf16 = False

# Use packing dataset creating
packing = False

# Enable gradient checkpointing
gradient_checkpointing = True

# Optimizer to use, original is paged_adamw_32bit
optim = "paged_adamw_32bit"

# Fraction of steps to do a warmup for
warmup_ratio = 0.03

# Log every X updates steps
logging_steps = 1

# Load the entire model on the GPU 0
device_map = {"": 0}

# Visualize training
report_to = "tensorboard"


#2. Import du tokenizer.
peft_config = LoraConfig(
    lora_alpha=lora_alpha,
    lora_dropout=lora_dropout,
    r=lora_r,
    inference_mode=False,
    task_type="CAUSAL_LM",
    target_modules = ["gate_proj", "down_proj", "up_proj", "q_proj", "v_proj", "k_proj", "o_proj"]
)

tokenizer = AutoTokenizer.from_pretrained(model_name)

# This is the fix for fp16 training
#tokenizer.padding_side = "right"
tokenizer.add_eos_token = True
tokenizer.pad_token = tokenizer.eos_token

#3. Préparation de la base de données

from datasets import load_dataset

def format_alpaca(sample):
    prompt = f"{sample['convervation']}"
    return prompt

# template dataset to add prompt to each sample
def template_dataset(sample):
    sample["text"] = f"{format_alpaca(sample)}"
    return sample

# Chargement du dataset.
data_files = {"train": "complete_debate_train_qwen.json"}
dataset = load_dataset("json", data_files=data_files, split="train")

# Shuffle the dataset
dataset_shuffled = dataset.shuffle(seed=42)

# Select the first 250 rows from the shuffled dataset, comment if you want 15k
#dataset = dataset_shuffled.select(range(512))

#Transformation du dataset pour utiliser le format guanaco
dataset = dataset.map(template_dataset, remove_columns=list(dataset.features))

# Select the first 250 rows from the shuffled dataset, comment if you want 15k
#dataset = dataset_shuffled.select(range(512))

print(dataset[40])

#4. Import du modèle

# Load tokenizer and model with QLoRA configuration
compute_dtype = getattr(torch, bnb_4bit_compute_dtype)

bnb_config = BitsAndBytesConfig(
    load_in_4bit=use_4bit,
    bnb_4bit_quant_type=bnb_4bit_quant_type,
    bnb_4bit_compute_dtype=compute_dtype,
    bnb_4bit_use_double_quant=use_nested_quant,
)

if compute_dtype == torch.float16 and use_4bit:
    major, _ = torch.cuda.get_device_capability()
    if major >= 8:
        print("=" * 80)
        print("Your GPU supports bfloat16, you can accelerate training with the argument --bf16")
        print("=" * 80)

model = AutoModelForCausalLM.from_pretrained(
    model_name,
    device_map="auto",
    quantization_config=bnb_config
)

model.config.use_cache = False
model.config.pretraining_tp = 1

tokenizer.chat_template = None

#5. Fine-tuning

torch.cuda.empty_cache()

def formatting_func(example):
    return example["text"]  # Your data is already properly formatted

training_arguments = SFTConfig(
    output_dir=output_dir,
    per_device_train_batch_size=per_device_train_batch_size,
    gradient_accumulation_steps=gradient_accumulation_steps,
    gradient_checkpointing=True,
    optim=optim,
    save_steps=save_steps,
    logging_steps=logging_steps,
    learning_rate=learning_rate,
    fp16=fp16,
    bf16=bf16,
    max_grad_norm=max_grad_norm,
    max_steps=max_steps,
    warmup_ratio=warmup_ratio,
    group_by_length=group_by_length,
    lr_scheduler_type=lr_scheduler_type,
    report_to="tensorboard",
    max_length=max_seq_length,
    packing=packing,
    # Remove dataset_text_field - we'll use formatting_func instead
)

trainer = SFTTrainer(
    model=model,
    train_dataset=dataset,
    peft_config=peft_config,
    processing_class=tokenizer,
    args=training_arguments,
    formatting_func=formatting_func,  # Add this instead of dataset_text_field
)

# Debug: Access the actual processed dataset that TRL will use for training
print("=== FINAL PROCESSED DATASET (what TRL actually uses) ===")
try:
    # Get the processed train dataset
    processed_dataset = trainer.train_dataset
    
    print(f"Dataset size: {len(processed_dataset)}")
    print(f"Dataset columns: {processed_dataset.column_names}")
    
    # Print a few samples of what's actually being fed to the model
    for i in range(min(3, len(processed_dataset))):
        print(f"\n--- Sample {i} ---")
        sample = processed_dataset[i]
        for key, value in sample.items():
            if key == "input_ids":
                # Decode the tokens to see the actual text
                decoded_text = tokenizer.decode(value, skip_special_tokens=False)
                print(f"{key}: {decoded_text}")
                print(f"{key} (raw tokens): {value[:50]}...")  # First 50 tokens
            elif key == "labels":
                # Show where labels are masked (-100) vs actual tokens
                print(f"{key}: {value[:50]}...")
            else:
                print(f"{key}: {value}")
        print("-" * 50)
    
except Exception as e:
    print(f"Error accessing processed dataset: {e}")
    print("Trying alternative method...")
    
    # Alternative: trigger dataset processing and inspect
    try:
        dataloader = trainer.get_train_dataloader()
        batch = next(iter(dataloader))
        print("First batch keys:", batch.keys())
        if "input_ids" in batch:
            sample_text = tokenizer.decode(batch["input_ids"][0], skip_special_tokens=False)
            print("Sample from first batch:")
            print(repr(sample_text))
    except Exception as e2:
        print(f"Alternative method also failed: {e2}")

trainer.train()

#Potentiellement switcher à resume_from_checkpoint si l'entraînement a été interrompu
#trainer.train(resume_from_checkpoint=True)

# 6. Sauvegarde
model_to_save = trainer.model.module if hasattr(trainer.model, 'module') else trainer.model
model_to_save.save_pretrained(new_model_name)
torch.cuda.empty_cache()

from peft import AutoPeftModelForCausalLM
model = AutoPeftModelForCausalLM.from_pretrained(new_model_name, device_map="auto", torch_dtype=torch.bfloat16)
model = model.merge_and_unload()

output_merged_dir = os.path.join(new_model_name, "merged_model")

# Fix specific to Gemma:
try:
    model.save_pretrained(output_merged_dir, safe_serialization=True)
except RuntimeError as e:
    if "share memory" in str(e):
        print("Shared tensor detected, saving without safe_serialization")
        model.save_pretrained(output_merged_dir, safe_serialization=False)
    else:
        raise e

tokenizer.save_pretrained(output_merged_dir)

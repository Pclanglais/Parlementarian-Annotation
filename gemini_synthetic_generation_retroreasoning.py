import base64
import os
import re
import pandas as pd
import json
from datetime import datetime
import time
from google import genai
from google.genai import types

def generate_gemini_completion(prompt):
    # Set up the request content
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt),
            ],
        ),
    ]
    
    # Configure response format
    generate_content_config = types.GenerateContentConfig(
        response_mime_type="text/plain",
    )
    
    # Generate content and collect response
    full_response = ""
    try:
        # For simplicity, we'll use the non-streaming version
        response = genai_client.models.generate_content(
            model="gemini-2.5-pro",
            contents=contents,
            config=generate_content_config,
        )
        full_response = response.text
    except Exception as e:
        print(f"Error generating content: {str(e)}")
        full_response = f"ERROR: {str(e)}"
    
    return full_response

# Set your API key - either in environment variable or directly
# os.environ["GEMINI_API_KEY"] = "your-api-key-here"  # Uncomment and set if not using env var
# Or initialize client with direct key
genai_client = genai.Client(
    api_key="[KEY]",
)

# Create output directory if it doesn't exist
output_dir = "projet/rag/gemini_profile_debate_reasoning"
os.makedirs(output_dir, exist_ok=True)


# Read your parquet file
result = pd.read_parquet("projet/rag/gemini_profile_reasoning.parquet")

def define_prompt(tag_entry, prediction, wikidata_label, biography):
    complete_prompt = f"""You have been submitted this discussion at the French parliamentary assembly:

{tag_entry}

As you notice all the actual speeches are annotated with tags and short contextual information.

Now {wikidata_label} is going to express itself. The speech is going to look like this:
{prediction}

What you need to do is write some kind of reasoning draft this person could write in his or her mind before talking. The draft should explicit the potential motivations, basically why is the person is using this modality of expression.

To help out, you have access to this short list of typical features this person is known for.
{biography}

The features can mix both psychological and discoursive characteristics.

The draft should follow some ground rules:
*stream of consciousness style, with some literary value. maybe try to assert first a style for the person in the analysis and stick to it in the draft.
*person can emit hypothesis about the tactic of the other protagonists to the discussion based on their past speech features.
*occasional context markers such as → for causal/logical flow, ? for uncertainty/questions to resolve, ! for key insights/breakthroughs, ≈ for approximations/estimates, ↺ for iterative verification across sources etc. You can especially use these when dealing with complex source triangulation.
*you can also use stenographic notation such as ※, NB for key insights, ∴ for conclusions, ?maybe? for tentative ideas, cf. for using quotes elements etc.

You should structure your output like this:
  
### Length ###
[Assess the length of the final speech and how long your analysis/draft should be as a result. If the text is short both your analysis and your draft should be **very** short. Allocate more inference time only for longer texts.]

### Analysis ###
[Analysis of all the submitted inputs, especially trying to interpret past interventions in light of the additional contextual information like the features. Try to assert also how the person could express themselves but **never** mention the actual speech.]

### Draft ###
[Draft of the person written in the first person trying to gradually build up the predicted speech. Style could be both inspired by what you know of their mode of expression from the features and their previous interventions if any. You can keep it in English.]
"""
    complete_prompt = re.sub("\n ", "\n", complete_prompt)
    return complete_prompt

def save_completion(prompt, entry, completion, index):
    # Prepare data to save
    data = {
        "chunk_id": entry["chunk_id"],
        "pivot_syceron": entry["pivot_syceron"],
        "wikidata_label": entry["wikidata_label"],
        "wikidata_id": entry["wikidata_id"],
        "tag_entry": entry["tag_entry"],
        "prediction": entry["prediction"],
        "biography": entry["biography"],
        "prompt": prompt,
        "completion": completion
    }
    
    # Create filename using search_id and index
    filename = f"{output_dir}/completion_{entry['pivot_syceron']}.json"
    
    # Save to JSON file
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    return filename

# Process each entry and get completion from Claude
for index, entry in result.iterrows():
    if 1==1:
        filename = f"{output_dir}/completion_{entry['pivot_syceron']}.json"

        if os.path.exists(filename):
            print(filename + " exists already.")
        else:
            tag_entry, prediction, wikidata_label, biography = entry["tag_entry"], entry["prediction"], entry["wikidata_label"], entry["biography"]
            prompt = define_prompt(tag_entry, prediction, wikidata_label, biography)
            
            completion_text = generate_gemini_completion(prompt)

            # Save the completion to a JSON file
            filename = save_completion(prompt, entry, completion_text, index)
            print(f"Saved completion {index + 1} to {filename}")
        
    else:
        print(f"Error processing entry {index + 1}: {str(e)}")
        continue

print("\nProcessing complete!")

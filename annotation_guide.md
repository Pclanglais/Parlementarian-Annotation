# French Parliamentary Debate Annotation Scheme

## Proposal Section

### Overview
The `<proposal>` element provides essential legislative context for each parliamentary debate, identifying the specific bill, law, or amendments under discussion. This section serves as the documentary header that situates the debate within the broader legislative process.

### Tag Structure
```xml
<proposal>
    <proposal_name>...</proposal_name>
    <proposal_name_original>...</proposal_name_original>
    <amendment>...</amendment>
    <law>...</law>
</proposal>
```

### Annotation Tags

#### 1. `<proposal_name>`
**Definition**: The English translation or descriptive title of the legislative proposal being discussed.
**Format**: Clear, descriptive title that captures the essence of the legislative matter.

**Usage**: Provides accessible identification of the subject matter for analysis purposes. Often includes procedural context (e.g., "Discussion of Article 6") or specific focus areas.

**Examples**:
- `<proposal_name>Right to Aid in Dying (Discussion of Article 6, Section 3)</proposal_name>`
- `<proposal_name>Contribution on Ultra-Processed Foods</proposal_name>`
- `<proposal_name>Emergency Bill for Mayotte</proposal_name>`
- `<proposal_name>Fighting child sexual abuse > Vote on the whole</proposal_name>`
- `<proposal_name>Student precariousness</proposal_name>`

#### 2. `<proposal_name_original>`
**Definition**: The original French title of the legislative proposal.
**Format**: Exact French parliamentary designation as it appears in official documents.

**Usage**: Preserves the authentic legislative reference and allows for precise identification within the French parliamentary system. Essential for cross-referencing with official records.

**Examples**:
- `<proposal_name_original>Droit à l'aide à mourir (Discussion des articles, Alinéa 3 de l'article 6)</proposal_name_original>`
- `<proposal_name_original>Contribution sur les produits alimentaires ultratransformés</proposal_name_original>`
- `<proposal_name_original>Projet de loi d'urgence pour Mayotte</proposal_name_original>`
- `<proposal_name_original>Lutter contre la pédocriminalité > Vote sur l'ensemble</proposal_name_original>`
- `<proposal_name_original>Précarité étudiante</proposal_name_original>`

### 3. `<amendment>`
**Definition**: Detailed description of specific amendments, modifications, or parliamentary proposals under discussion.
**Format**: Structured enumeration of amendments with numbers, sponsors, and brief descriptions of their content.

**Examples**:

*Simple Amendment:*
```xml
<amendment>Amendement no 2307</amendment>
```

*Complex Amendment Structure:*
```xml
<amendment>Unnamed amendment proposed by Stella Dupont to remove Section 3 of Article 6.
    *   Amendment no. 44 by Patrick Hetzel (aiming to introduce judicial review for doubts regarding free and informed consent).
    *   Amendment no. 45 by Patrick Hetzel (aiming to exclude persons with psychiatric illnesses).</amendment>
```

#### 4. `<law>`
**Definition**: The broader legislative framework or bill within which the debate takes place.
**Format**: Official designation of the law or bill, often including specific identifying numbers.

**Usage**: Provides the formal legislative context that frames the specific amendments or discussions. Essential for understanding the scope and significance of the debate.

**Examples**:
- `<law>Projet de loi de financement de la sécurité sociale pour 2025</law>`
- `<law>Projet de loi de 2024 (as referenced by the government and speakers, indicating a bill currently under discussion).</law>`
- `<law>Article 3 of the law concerning "Droit à l'aide à mourir"</law>`

## Speech Section

### Overview
Each `<speech>` element contains annotations for individual parliamentary interventions, identified by a unique identifier and speaker name. The speech section captures the rhetorical, emotional, and argumentative dimensions of parliamentary discourse.

### Tag Structure
```xml
<speech identifier="[unique_id]" name="[speaker_name]">
    <!-- Multiple annotation tags -->
</speech>
```

### Annotation Tags

#### 1. `<stance>`
**Definition**: The speaker's positioning relative to the topic, amendment, or other speakers.
**Values**:
- `Assertive` - Confidently presenting a position
- `Defensive` - Responding to criticism or attacks
- `Offensive` - Actively attacking positions or opponents
- `Supportive` - Expressing agreement or backing
- `Opposed` - Expressing disagreement or opposition
- `Neutral` - Maintaining institutional neutrality
- `Facilitative` - Managing debate flow (often procedural roles)
- `Cooperative` - Working collaboratively
- `Dismissive` - Rejecting arguments or positions
- `Challenging` - Questioning or confronting
- `Critical` - Evaluating negatively
- `Confirming` - Validating or reinforcing

**Usage**: Multiple stance tags can be applied to capture complex positioning. Often qualified with contextual information in parentheses.

**Examples**:
- `<stance>Opposed</stance>` - Simple opposition
- `<stance>Opposed , Assertive (to government's view)</stance>` - Qualified opposition
- `<stance>Defensive</stance><stance>Assertive</stance>` - Multiple stances

#### 2. `<emotion>`
**Definition**: The emotional tone expressed by the speaker.
**Values**:
- `Neutral` - No particular emotional coloring
- `Passionate` - Intense, fervent expression
- `Aggressive` - Hostile or combative tone
- `Sarcastic` - Ironic or mocking tone
- `Dismissive` - Contemptuous or disdainful
- `Positive` - Optimistic or encouraging
- `Negative` - Pessimistic or critical
- `Assertive` - Confident and forceful
- `Concerned` - Worried or troubled

**Usage**: Can have multiple emotion tags. Sometimes qualified with specific quotes.

**Examples**:
- `<emotion>Sarcastic [""C'est grâce à la gauche !""]</emotion>`
- `<emotion>Aggressive</emotion><emotion>Passionate</emotion>`

#### 3. `<epistemic_frame>`
**Definition**: The type of knowledge or reasoning framework invoked by the speaker.
**Values**:
- `Procedure/law` - Legal, procedural, or regulatory arguments
- `Figures` - Statistical or numerical evidence
- `Common sense` - Appeal to obvious or intuitive reasoning
- `Practical necessity` - Arguments based on practical needs
- `Daily life` - References to everyday experience
- `Personal testimony` - First-hand experience or anecdotal evidence
- `Historical reference` - Appeals to historical precedent
- `Will of the people` - Democratic legitimacy arguments
- `Values/Ideology` - Moral or ideological principles
- `Principles` - General philosophical principles
- `Threat` - Warnings or dire predictions
- `national heritage/value` - Appeals to national identity

**Usage**: Always includes bracketed quotes showing the specific textual evidence.

**Examples**:
- `<epistemic_frame>Procedure/law [""remettent en cause le pacte Dutreil""]</epistemic_frame>`
- `<epistemic_frame>Figures [""200 milliards d'euros""]</epistemic_frame>`

#### 4. `<debate_adherence>`
**Definition**: How the speaker relates to debate norms and procedures.
**Values**:
- `Respectful` - Following parliamentary etiquette
- `Disruption` - Breaking or challenging debate norms
- `Digression` - Going off-topic or procedural deviation
- `Adherence` / `Adherent` - Conforming to debate rules

**Usage**: Sometimes qualified with specific examples in brackets.

**Examples**:
- `<debate_adherence>Disruption [""150 ou 200 amendements""]</debate_adherence>`
- `<debate_adherence>Respectful</debate_adherence>`

#### 5. `<argumentative_structure>`
**Definition**: The rhetorical or logical structure of the intervention.
**Values**:
- `Reaction` - Responding to previous interventions
- `Explaining government's position` - Official governmental stance
- `Call to action` - Urging specific actions
- `Enumeration` - Listing points or arguments
- `Direct accusation` - Making explicit accusations
- `Counter-argumentation` - Systematic refutation
- `Explaining the problem` - Problem identification and analysis
- `Defending` - Protecting a position or policy
- `Structured argument` - Organized logical presentation
- `Personal testimony` - Using personal experience as evidence

**Usage**: Multiple tags can describe complex rhetorical structures.

**Examples**:
- `<argumentative_structure>Enumeration</argumentative_structure><argumentative_structure>Call to action</argumentative_structure>`

#### 6. `<performative_act>`
**Definition**: What the speaker is doing through their speech (speech acts).
**Values**:
- `Give the floor` - Procedural floor management
- `Request an opinion` - Asking for positions
- `Call to vote` - Initiating voting procedures
- `Announce vote results` - Declaring outcomes
- `Recommending a vote` - Advising voting behavior
- `Requesting withdrawal of amendments` - Procedural requests
- `Call to action` - Urging specific actions
- `Clarification` - Providing explanations

**Usage**: Often includes specific contextual details in parentheses.

**Examples**:
- `<performative_act>Call to action (France must support, IRGC on EU terror list)</performative_act>`
- `<performative_act>Give the floor</performative_act>`

#### 7. `<audience>`
**Definition**: Who the speaker is primarily addressing.
**Values**:
- `General public` - Broader public audience
- `Government` - Executive branch
- `Opponent` - Political adversaries
- `Ally` - Political supporters
- `Institutional role` - Specific parliamentary roles
- Individual names - Direct address to specific members

**Usage**: Can specify multiple audiences. Sometimes qualified with names or roles.

**Examples**:
- `<audience>Government (France/EU)</audience>`
- `<audience>Opponent (Jean-Philippe Tanguy)</audience>`

#### 8. `<figure_of_speech>`
**Definition**: Rhetorical devices and stylistic elements used.
**Values**:
- `Metaphor` - Figurative comparisons
- `Hyperbole` - Exaggeration for effect
- `Repetition` - Repeated words or phrases
- `Apostrophe` - Direct address
- `Antithesis` - Contrasting ideas
- `Rhetorical question` - Questions for effect
- `Synecdoche` - Part representing whole
- `Enumeration` - Structured listing
- `Anaphora` - Repetition at beginning of clauses
- `Sarcasm` - Ironic expression

**Usage**: Always includes bracketed quotes showing the specific textual evidence.

**Examples**:
- `<figure_of_speech>Metaphor [""cette prison de tissu""]</figure_of_speech>`
- `<figure_of_speech>Hyperbole [""une fois, deux fois, dix fois""]</figure_of_speech>`

#### 9. `<support>`
**Definition**: Explicit backing or agreement with other speakers or positions.
**Values**: References to specific speakers, amendments, or positions.

**Usage**: Includes specific references, often with speech identifiers.

**Examples**:
- `<support>Ayda Hadizadeh (#3614643)</support>`
- `<support>Jean-Paul Mattei's amendment [""en faveur de l'amendement no 3590""]</support>`

#### 10. `<attack>`
**Definition**: Explicit criticism or opposition to other speakers or positions.
**Values**: References to specific speakers, amendments, or positions being criticized.

**Usage**: Similar format to support, with specific references and sometimes quoted critiques.

**Examples**:
- `<attack>Laurent Saint-Martin (#3527393)</attack>`
- `<attack>Éva Sas's amendment [""votez contre l'amendement no 785""]</attack>`

#### 11. `<reference>`
**Definition**: Mentions or citations of other speakers, documents, or legislative elements.
**Values**: Names, speech identifiers, legislative references.

**Usage**: Used for neutral mentions that aren't explicitly supportive or attacking.

**Examples**:
- `<reference>François Gernigon (#3550027)</reference>`
- `<reference>Naïma Moutchou (#3550031)</reference>`

#### 12. `<text_editing>`
**Definition**: Proposed textual modifications to legislation or amendments.
**Values**: 
- `Remove` - Deletion proposals
- `Change` - Modification proposals
- `Add` - Addition proposals

**Usage**: Includes bracketed quotes showing the specific text being modified.

**Examples**:
- `<text_editing>Remove [""remettent en cause le pacte Dutreil""]</text_editing>`
- `<text_editing>Change [""trois mois""]</text_editing>`

### Notes on Usage

1. **Multiple Tags**: Most elements can have multiple instances to capture the complexity of parliamentary discourse.

2. **Contextual Qualifiers**: Many tags include parenthetical qualifications or bracketed quotes to provide specific textual evidence.

3. **Cross-References**: The scheme uses speech identifiers (e.g., #3550027) to create links between interventions.

4. **Hierarchical Structure**: Tags work together to create a comprehensive picture of each speech act within the parliamentary context.

5. **Flexibility**: The scheme accommodates both formal procedural language and heated political exchanges, capturing the full spectrum of parliamentary discourse.


## Debate Section

### Overview
The `<debate>` element provides a comprehensive meta-level analysis of the entire parliamentary exchange, capturing the thematic content, procedural context, emotional atmosphere, political dynamics, and outcomes of the debate.

### Tag Structure
```xml
<debate>
    <topics>...</topics>
    <debate_type>...</debate_type>
    <tone>...</tone>
    <coalition_dynamics>...</coalition_dynamics>
    <debate_resolution>...</debate_resolution>
    <vote_resolution>...</vote_resolution>
</debate>
```

### Annotation Tags

#### 1. `<topics>`
**Definition**: The substantive themes and subject matters discussed during the debate.
**Format**: Free-text enumeration of topics, typically separated by line breaks or presented as a narrative list.

**Usage**: Captures both the primary legislative focus and secondary themes that emerge during discussion. Topics can range from specific policy details to broader procedural and political issues.

**Examples**:
```xml
<topics>
Health risks of ultra-processed foods (cancers, cardiovascular diseases, type 2 diabetes)
Public health policy and prevention strategies
Taxation/contribution on specific products
Legislative procedure: amendment definition, impact studies, modalities of implementation
Nova food classification
Collaboration with the agri-food industry
</topics>
```

```xml
<topics>
Taxation of workers
Taxation of retirees
Fairness in taxation
Contribution of workers and retirees to national solidarity
</topics>
```

#### 2. `<debate_type>`
**Definition**: The procedural and functional category of the parliamentary exchange.
**Values**:

##### Primary Types:
- **Construction of a law article** - Formal legislative drafting and amendment discussions
- **Questions au gouvernement** - Government Q&A sessions
- **Polemics** - Confrontational political exchanges
- **Government declaration** - Executive policy announcements
- **Presentation of a law proposal** - Introduction of new legislation
- **Vote on the whole** - Final passage votes

##### Combined/Qualified Types:
- **Questions au gouvernement > Polemics** - Q&A sessions that become confrontational
- **Construction of a law article > Polemics** - Legislative work with significant conflict
- **Questions to the government (Q&A), Polemic** - Multiple procedural contexts

**Usage**: Can include specific qualifications in parentheses to provide additional context about the nature or focus of the debate.

**Examples**:
- `<debate_type>Construction of a law article (discussion and vote on an amendment to a financing bill)</debate_type>`
- `<debate_type>Questions au Gouvernement > Polemics (highly confrontational exchanges)</debate_type>`
- `<debate_type>Polemics (Questions au gouvernement)</debate_type>`

#### 3. `<tone>`
**Definition**: The overall emotional and interactional atmosphere of the debate.
**Values**:

#### Single Descriptors:
- `Neutral` - Professional, unemotional discourse
- `Constructive` - Collaborative, solution-oriented
- `Confrontational` - Adversarial and argumentative
- `Chaotic` - Disorderly, with multiple interruptions
- `Respectful` - Maintaining parliamentary decorum

#### Complex/Evolving Tones:
- `Neutral to constructive` - Progressive improvement in atmosphere
- `Chaotic (initial banter) > Neutral (as formal proceedings resume)` - Temporal evolution
- `Chaotic and confrontational (marked by frequent interjections, exclamations, and direct personal attacks)`

**Usage**: Often includes specific descriptive details in parentheses explaining the characteristics that define the tone.

**Examples**:
- `<tone>Neutral to constructive. The exchange is formal and follows parliamentary procedure, with no overt aggression or personal attacks. The government's opposition is explained calmly and rationally.</tone>`
- `<tone>Chaotic and confrontational (marked by frequent interjections, exclamations, and direct personal attacks).</tone>`

#### 4. `<coalition_dynamics>`
**Definition**: The political positioning and interactions of different speakers, parties, and groups during the debate.
**Format**: Structured list identifying each participant with their political affiliation and stance.

#### Participant Identification:
- **Individual names** with party/role affiliation in parentheses
- **Party/group abbreviations** (LFI-NFP, EPR, DR, RN, etc.)
- **Role descriptions** (Member of French Government, Representative of...)

#### Stance Categories:
- `Proposed` - Initiating or advocating for the measure
- `Opposed` - Against the measure or position
- `Supportive` - Backing other speakers or positions
- `Facilitated` - Managing procedural aspects
- `Neutral` - Maintaining institutional neutrality
- `Defensive` - Responding to attacks or criticism

**Usage**: Each entry typically follows the format: "Name (Affiliation): Stance (with qualification/explanation)". Complex dynamics can be captured with multiple stance indicators.

**Examples**:
```xml
<coalition_dynamics>
François Gernigon (center-right independent party): Proposed (amendment no 2307)
Naïma Moutchou (center-right independent party): Facilitated (as chair of the session)
Yannick Neuder (Member of French Government): Opposed
Geneviève Darrieussecq (Representative of centrist party (Les Démocrates)): Opposed (explained the government's position)
</coalition_dynamics>
```

```xml
<coalition_dynamics>
Front Populaire (LFI-NFP): Proposed (the abrogation law), Opposed (to the blocking tactics by the majority), Assertive (demanding substantive debate)
Manuel Bompard: Proposed > Opposed (to blocking) > Assertive (for substantive debate)
Center-right independent party (Naïma Moutchou): Facilitated (presiding the session), but her actions align with the procedural tactics employed by the majority
</coalition_dynamics>
```

#### 5. `<debate_resolution>`
**Definition**: The substantive outcome or conclusion of the debate in terms of the underlying policy or political question.
**Values**:

#### Definitive Outcomes:
- `Positive` - Favorable resolution of the main issue
- `Negative` - Unfavorable resolution or rejection
- `Interrupted/Stalled` - Debate halted without conclusion
- `Suspended` - Temporarily postponed

#### Non-Applicable Cases:
- `Non-applicable` - For formats that don't seek resolution (Q&A sessions, declarations)

**Usage**: Often includes detailed explanations of what specifically was resolved and any nuances or future implications.

**Examples**:
- `<debate_resolution>Negative (the specific amendment was rejected). However, the explanation provided by the government suggests that the underlying issue might be addressed in future work, possibly through different means or after further study.</debate_resolution>`
- `<debate_resolution>Non-applicable (as a "Question au Gouvernement," it's not designed for a formal resolution; this specific exchange appears to be cut short by calls for order, suggesting it was effectively interrupted).</debate_resolution>`

#### 6. `<voice_resolution>`
**Definition**: The formal voting outcome when a parliamentary vote occurs.
**Values**:

#### Vote Outcomes:
- `Positive` - Motion/amendment adopted
- `Negative` - Motion/amendment rejected  
- `Suspended` - Vote postponed or incomplete

#### Non-Applicable Cases:
- `Non-applicable` - When no formal vote takes place

**Usage**: Typically includes specific details about what was voted on and sometimes vote counts when available.

**Examples**:
- `<vote_resolution>Negative (amendment no 2307 was rejected).</vote_resolution>`
- `<vote_resolution>Negative (The amendments to suppress Article 17 were rejected, with 83 votes against their adoption and 51 votes for). This means Article 17, establishing the "délit d'entrave," remains in the bill.</vote_resolution>`
- `<vote_resolution>Non-applicable.</vote_resolution>`

### Debate Type Categories

#### Legislative Debates
- **Construction of a law article**: Formal amendment and article-by-article examination
- **Presentation of a law proposal**: Introduction of new legislation
- **Vote on the whole**: Final passage considerations

#### Executive-Legislative Interactions  
- **Questions au gouvernement**: Regular government accountability sessions
- **Government declaration**: Executive policy announcements and reactions

#### Confrontational Exchanges
- **Polemics**: Highly adversarial political debates
- **Questions au gouvernement > Polemics**: Q&A sessions that become confrontational

### Usage Notes

1. **Temporal Evolution**: The tone and dynamics can evolve during a debate, captured through sequential descriptions (e.g., "Chaotic > Neutral").

2. **Multi-dimensional Analysis**: Coalition dynamics capture both the formal political affiliations and the actual behavioral stances during the specific debate.

3. **Procedural Context**: The debate_type provides crucial context for interpreting the significance and constraints of the exchange.

4. **Resolution Distinction**: The scheme distinguishes between substantive debate outcomes (debate_resolution) and formal parliamentary votes (vote_resolution).

5. **Non-Applicable Categories**: Many parliamentary formats (especially Q&A sessions) don't aim for formal resolutions, appropriately marked as "Non-applicable."

6. **Detailed Explanations**: Most tags include extensive explanatory text to capture the nuanced reality of parliamentary dynamics that can't be reduced to simple categorical labels.

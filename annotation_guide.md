## French Parliamentary Debate Annotation Scheme - Speech Section

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

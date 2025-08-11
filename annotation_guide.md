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
**Definition**: The speaker's positioning regarding the proposal being discussed.

**Values**:
- `Offensive` - Actively attacking the proposal or opposing positions
- `Defensive` - Responding to criticism or protecting a position
- `Assertive` - Confidently presenting a position on the proposal
- `Supportive` - Expressing agreement or backing for the proposal
- `Opposed` - Expressing disagreement or opposition to the proposal
- `Neutral` - Maintaining institutional neutrality
- `Facilitative` - Managing debate flow (often procedural roles)
- `Consensus-seeking` - Working toward agreement or compromise
- `Dismissive` - Rejecting the proposal or arguments
- `Challenging` - Questioning or confronting the proposal
- `Critical` - Evaluating the proposal negatively
- `Confirming` - Validating or reinforcing the proposal

**Usage**: Multiple stance tags can be applied to capture complex positioning. Often qualified with contextual information in parentheses.

**Examples**:
- `<stance>Opposed</stance>` - Simple opposition to the proposal
- `<stance>Supportive, Assertive (regarding amendment 785)</stance>` - Qualified support
- `<stance>Defensive</stance><stance>Critical</stance>` - Multiple stances

#### 2. `<epistemic_claim>`
**Definition**: The type of knowledge or evidence framework invoked by the speaker.

The fields from this category were partly built on top of the work of Bernard Reber.

**Values**:
- `Expert knowledge` - Professional or technical expertise
- `Figures` - Statistical or numerical evidence
- `Institutional knowledge` - Knowledge of procedures, precedents, or institutional memory
- `Historical reference` - Appeals to historical precedent or events
- `Will of the people` - Democratic legitimacy arguments
- `Common sense` - Appeal to obvious or intuitive reasoning
- `Lived experience` - Personal or community experience
- `Practical necessity` - Arguments based on practical needs
- `Personal testimony` - First-hand experience or anecdotal evidence
- `Values/Ideology` - Moral or ideological principles
- `Principles` - General philosophical principles
- `Contested facts` - Disputed or controversial information

**Usage**: Always includes bracketed quotes showing the specific textual evidence.

**Examples**:
- `<epistemic_claim>Expert knowledge ["according to constitutional scholars"]</epistemic_claim>`
- `<epistemic_claim>Figures ["200 billion euros"]</epistemic_claim>`
- `<epistemic_claim>Will of the people ["the citizens have clearly expressed their will"]</epistemic_claim>`

#### 3. `<deliberative_quality>`
**Definition**: Assessment of the contribution's quality to democratic deliberation.

**Values**:
- `Justified` - Claims are supported with reasons and evidence
- `Responsive` - Builds meaningfully on previous contributions
- `Civil` - Maintains respectful discourse
- `Position-changing` - Shows evolution or modification of views
- `Dismissive` - Ignores or dismisses opposing arguments without engagement
- `Repetitive` - Repeats previous points without new reasoning

**Usage**: Multiple tags can assess different aspects of deliberative quality.

**Examples**:
- `<deliberative_quality>Justified</deliberative_quality><deliberative_quality>Responsive</deliberative_quality>`
- `<deliberative_quality>Dismissive ["I won't even dignify that with a response"]</deliberative_quality>`

#### 4. `<emotional_valence>`
**Definition**: The emotional tone expressed by the speaker.

**Values**:
- `Neutral` - No particular emotional coloring
- `Aggressive` - Hostile or combative tone
- `Sarcastic` - Ironic or mocking tone
- `Passionate` - Intense, fervent expression
- `Concerned` - Worried or troubled
- `Critical` - Evaluative and fault-finding
- `Accusatory` - Blaming or charging with fault
- `Frustrated` - Showing annoyance or impatience
- `Firm` - Resolute and unwavering
- `Impatient` - Showing restlessness or urgency
- `Indignant` - Showing anger at perceived injustice
- `Enthusiastic` - Showing excitement or eagerness
- `Determined` - Showing resolve and purpose
- `Humorous` - Using humor or wit
- `Disappointed` - Showing sadness or dissatisfaction
- `Regretful` - Showing remorse or sorrow
- `Exasperated` - Showing extreme frustration

**Usage**: Can have multiple emotion tags. Sometimes qualified with specific quotes.

**Examples**:
- `<emotional_valence>Sarcastic ["Thanks to the left, of course!"]</emotional_valence>`
- `<emotional_valence>Passionate</emotional_valence><emotional_valence>Indignant</emotional_valence>`

#### 5. `<debate_adherence>`
**Definition**: How the speaker relates to debate norms, procedures, and framing.

**Values**:
- `Disruption` - Breaking or challenging debate norms significantly
- `Digression` - Slight deviation but still within the same theme
- `Respectful` - Following parliamentary etiquette
- `Adherence` - Conforming to debate rules and procedures
- `Procedural` - Focusing on procedural matters
- `Confrontational` - Engaging in direct conflict or opposition
- `Constructive` - Contributing positively to the debate process
- `Maintaining order` - Working to preserve debate structure

**Usage**: Sometimes qualified with specific examples in brackets.

**Examples**:
- `<debate_adherence>Disruption ["150 or 200 amendments"]</debate_adherence>`
- `<debate_adherence>Constructive</debate_adherence><debate_adherence>Respectful</debate_adherence>`

#### 6. `<argumentative_structure>`
**Definition**: The rhetorical or logical structure of the intervention.

**Values**:
- `Personal testimony` - Using personal experience as evidence
- `Reaction` - Responding to previous interventions
- `Explaining government's position` - Official governmental stance
- `Call to action` - Urging specific actions
- `Enumeration` - Listing points or arguments systematically
- `Direct accusation` - Making explicit accusations
- `Counter-argumentation` - Systematic refutation of opposing views
- `Explaining the problem` - Problem identification and analysis
- `Rhetorical question` - Using questions for persuasive effect
- `Justification` - Providing reasons and support for positions
- `Rebuttal` - Responding to and refuting opposing arguments
- `Problem-solution` - Identifying problems and proposing solutions

**Usage**: Multiple tags can describe complex rhetorical structures.

**Examples**:
- `<argumentative_structure>Problem-solution</argumentative_structure><argumentative_structure>Call to action</argumentative_structure>`
- `<argumentative_structure>Rhetorical question ["How can we ignore such evidence?"]</argumentative_structure>`

#### 7. `<audience>`
**Definition**: Who the speaker is primarily addressing or targeting.

**Values**:
- `Opponents` - Political adversaries or those with opposing views
- `Allies` - Political supporters or those with aligned views
- `Citizens` - General public or electorate
- `Civil society` - NGOs, associations, organized groups
- `Future generations` - Those who will be affected in the future
- `Affected populations` - Specific groups impacted by the proposal
- `Government` - Executive branch or ministers
- `Institutional roles` - Specific parliamentary roles or positions

**Usage**: Can specify multiple audiences. Sometimes qualified with names or specific groups.

**Examples**:
- `<audience>Citizens</audience><audience>Affected populations (farmers)</audience>`
- `<audience>Government (Minister of Finance)</audience>`

#### 8. `<figure_of_speech>`
**Definition**: Rhetorical devices and stylistic elements used by the speaker.

**Values**:
- `Metaphor` - Figurative comparisons
- `Anaphora` - Repetition at the beginning of successive clauses
- `Analogy` - Comparison to explain or clarify
- `Hyperbole` - Exaggeration for effect
- `Understatement/litote` - Deliberate understatement or negation
- `Enumeration` - Structured listing for emphasis
- `Repetition` - Repeated words or phrases
- `Antithesis` - Contrasting ideas or concepts
- `Parallelism` - Similar grammatical structures
- `Apostrophe` - Direct address to someone not present
- `Climax` - Building to a crescendo or peak
- `Aposiopesis` - Deliberate breaking off of speech
- `Apophasis` - Mentioning by claiming not to mention
- `Polysyndeton` - Deliberate use of many conjunctions
- `Chiasmus` - Reversal of grammatical structures
- `Synecdoche` - Part representing the whole

**Usage**: Always includes bracketed quotes showing the specific textual evidence.

**Examples**:
- `<figure_of_speech>Metaphor ["this prison of fabric"]</figure_of_speech>`
- `<figure_of_speech>Anaphora ["We must act, we must decide, we must move forward"]</figure_of_speech>`
- `<figure_of_speech>Hyperbole ["once, twice, ten times"]</figure_of_speech>`

#### 9. `<support>`
**Definition**: Explicit backing or agreement with other speakers or positions.

**Values**: References to specific speakers with their full names and specific id_syceron.

**Usage**: Always includes the complete name of the person and their speech identifier.

**Examples**:
- `<support>Ayda Hadizadeh (#3614643)</support>`
- `<support>Jean-Paul Mattei (#3527401) [supporting amendment 3590]</support>`

#### 10. `<attack>`
**Definition**: Explicit criticism or opposition to other speakers or positions.

**Values**: References to specific speakers with their full names and specific id_syceron being criticized.

**Usage**: Always includes the complete name of the person and their speech identifier.

**Examples**:
- `<attack>Laurent Saint-Martin (#3527393)</attack>`
- `<attack>Éva Sas (#3550045) [opposing amendment 785]</attack>`

#### 11. `<reference>`
**Definition**: Neutral mentions or citations of other speakers, documents, or legislative elements.

**Values**: Full names of people with their specific id_syceron for neutral references.

**Usage**: Used for neutral mentions that aren't explicitly supportive or attacking.

**Examples**:
- `<reference>François Gernigon (#3550027)</reference>`
- `<reference>Naïma Moutchou (#3550031)</reference>`

#### 12. `<performative_act>`
**Definition**: Actual actions performed through the speaker's intervention.

**Values**:
- `Call to vote` - Initiating voting procedures
- `Announce vote result` - Declaring voting outcomes
- `Recommend a vote` - Advising specific voting behavior
- `Request an opinion` - Asking for positions or views
- `Call to speak` - Inviting someone to speak
- `Call for speaker` - Requesting a specific speaker
- `Ask for opinion` - Soliciting views or positions
- `Ask for government's opinion` - Requesting official government position
- `Call for opinion` - General request for viewpoints
- `Give an opinion` - Providing a position or view
- `Call for order` - Requesting adherence to procedures
- `Support an amendment` - Backing specific legislative changes
- `Cede the floor` - Giving up speaking time
- `Suspend the session` - Pausing proceedings
- `Open the session` - Beginning proceedings
- `Resume the session` - Continuing after suspension
- `Allocate floor time` - Assigning speaking time
- `Submit an amendment` - Proposing legislative changes
- `Bring a formal complaint` - Making official objections
- `Give the floor` - Granting speaking permission
- `Request withdrawal of amendment` - Asking for amendment removal
- `Clarification` - Providing explanations or corrections

**Usage**: Often includes specific contextual details in parentheses.

**Examples**:
- `<performative_act>Call to vote (amendment 3590)</performative_act>`
- `<performative_act>Request withdrawal of amendment (no. 785)</performative_act>`

#### 13. `<text_editing>`
**Definition**: Specific textual modifications proposed for legislation or amendments.

**Values**: 
- `ADD ("[text to add]")` - Proposed additions to text
- `REMOVE ("[text to remove]")` - Proposed deletions from text
- `CHANGE ("[text to change]")` - Proposed modifications to text

**Usage**: Always includes the specific text being modified in brackets using the standardized formulas.

**Examples**:
- `<text_editing>REMOVE ("[text that undermines the Dutreil pact]")</text_editing>`
- `<text_editing>ADD ("[within three months]")</text_editing>`
- `<text_editing>CHANGE ("[from six months to three months]")</text_editing>`

### Notes on Usage

1. **Multiple Tags**: Most elements can have multiple instances to capture the complexity of parliamentary discourse.

2. **Contextual Qualifiers**: Many tags include parenthetical qualifications or bracketed quotes to provide specific textual evidence.

3. **Cross-References**: The scheme uses speech identifiers (e.g., #3550027) with complete speaker names to create links between interventions.

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

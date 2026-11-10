"""Additional original units addressing gaps found in the first coverage audit."""
from course_authoring import unit

UNITS = {
"starter": [
unit("s17", "Food, drinks and likes", "A1", "vocabulary", "Name common food and express a simple preference.",
"Food words: bread, rice, egg, apple, banana. Drinks: water, milk, tea, coffee. Use I like + noun to express a preference: I like rice. Use I don't like ... for a negative. Ask Do you like tea? Answer Yes, I do / No, I don't. Like is not the same as want: a general preference differs from a request now.",
"Sort words into food and drink. Then make a preference: I like tea. For a request now, say Tea, please. To ask another person's preference, start Do you like ...?",
"""Which is a drink? | water | bread | egg | 0 | Water is a drink.
Choose a preference. | I am rice. | I like rice. | I rice like am. | 1 | Like expresses a preference.
Choose the negative. | I not like tea. | I am don't tea. | I don't like tea. | 2 | Use don't + like.
Ask about a preference. | Do you like coffee? | Are you coffee? | Where coffee like? | 0 | Do you like asks about preference.
Do you like apples? — Yes, I ___. | am | do | is | 1 | Use do in the short answer.
Which is food rather than a drink? | tea | milk | bread | 2 | Bread is food.
Which requests something now? | Water, please. | I like water generally. | Water is clear. | 0 | The phrase makes a request.""",
"Write a simple menu and a four-line conversation about likes and an order."),
unit("s18", "Home, clothes and personal items", "A1", "vocabulary", "Recognise everyday nouns and place them in a simple description.",
"Home: kitchen, bedroom, bathroom, door, window. Clothes: shirt, coat, shoes. Personal items: phone, key, bag. A bedroom is a room for sleeping. Shoes are worn on feet. A key can open a lock. Combine the words with familiar patterns: My shoes are in the bedroom. This is my coat.",
"Group words by use, not only spelling: rooms → kitchen/bedroom; clothes → coat/shoes; carried items → phone/key. Then locate one item using in, on or under.",
"""A room for sleeping is a: | bedroom | shoe | key | 0 | Bedroom names a sleeping room.
You wear these on your feet: | windows | shoes | kitchens | 1 | Shoes are footwear.
Which can open a lock? | a shirt | a bedroom | a key | 2 | A key operates a lock.
Which is clothing? | a coat | a door | a kitchen | 0 | A coat is worn.
Choose the correct plural sentence. | My shoes is here. | My shoes are here. | My shoes am here. | 1 | Shoes takes are.
Which names a room? | phone | bag | bathroom | 2 | Bathroom is a room.
Choose a personal item. | a phone | a kitchen | a bedroom | 0 | A phone is a personal item.""",
"Describe a fictional home and locate five personal items in it."),
unit("s19", "Weather and feelings", "A1", "vocabulary", "Describe weather and a basic personal state.",
"Weather: sunny, rainy, windy, cold, hot. Use it for weather: It's sunny. It's cold today. Feelings and states: happy, sad, tired, hungry, thirsty. Use I am: I'm tired. Hungry means wanting food; thirsty means wanting a drink. Do not use I for the general weather unless you mean your own feeling of temperature.",
"Choose the subject first: outside conditions → it; your state → I. It's rainy describes weather. I'm tired describes you. Match hungry with food and thirsty with a drink.",
"""Describe general weather. | It's sunny. | I sunny. | Sunny am. | 0 | Use it is for weather.
Wanting a drink means: | hungry | thirsty | windy | 1 | Thirsty means needing or wanting a drink.
Wanting food means: | rainy | cold outside | hungry | 2 | Hungry relates to food.
Describe your state. | I'm tired. | It tired me am. | I tired is. | 0 | I am + adjective describes the speaker.
Which is a weather word? | sister | rainy | key | 1 | Rainy describes weather.
Opposite of hot: | happy | sunny | cold | 2 | Hot and cold contrast in temperature.
Which distinguishes weather from a personal feeling? | It's cold outside, and I'm cold too. | I am outside weather. | Weather is my name. | 0 | It describes conditions; I describes the speaker.""",
"Write a three-day weather diary with one personal feeling or state for each day."),
unit("s20", "Forms, names and contact details", "A1", "literacy", "Identify common fields in a simple form without sharing real private data.",
"Forms often ask for first name, family name, date of birth and contact details. First name is a given name; family name is a surname. Email addresses include @ and a domain. A postcode identifies a postal area. Practise with fictional details, not your real address, password or phone number. Read the field label before entering information.",
"Match label to information. First name → Jo. Family name → Green. Email → a fictional address. A password is not the same as a public name; never put one into a learning exercise.",
"""First name usually means: | given name | postal area | password | 0 | It is a personal given name.
Family name means: | age | surname | street only | 1 | Family name and surname are synonyms here.
An email address normally contains: | only a day name | only a colour | @ | 2 | @ separates the local part and domain.
A date-of-birth field asks for: | when a person was born | their favourite colour | tomorrow's weather | 0 | Date of birth identifies the birth date.
For this practice, use: | your account password | fictional details | another person's private address | 1 | Fictional details are sufficient for learning.
A postcode identifies: | a family relationship | a verb tense | a postal area | 2 | Postcodes support postal addressing.
What should you read first? | the field label | an unrelated advertisement | a hidden password | 0 | The label tells you what information belongs there.""",
"Create a fictional profile with a given name, surname, invented contact label and birth date; do not use real private information."),
],
"beginner": [
unit("b17", "Do/does questions and short answers", "A1", "grammar", "Ask about routines with the correct auxiliary.",
"Use Do + I/you/we/they + base verb? Use Does + he/she/it + base verb? Do you work here? Does she work here? Does already marks the third person: do not add -s to work. Short answers repeat the auxiliary: Yes, she does. No, they don't. Questions with be use inversion instead: Is she ready?",
"Find the main verb. Work is an action verb: Does she work? Ready follows be: Is she ready? Do not combine does with works, or use does as an extra auxiliary before is.",
"""___ you work here? | Do | Does | Is | 0 | You takes do with work.
___ she study English? | Do | Does | Are | 1 | She takes does.
Choose the correct question. | Does she works here? | Do she work here? | Does she work here? | 2 | Does takes the base verb.
Does he cook? — Yes, he ___. | does | do | is | 0 | Repeat does in the short answer.
Do they drive? — No, they ___. | doesn't | don't | aren't cooking | 1 | They takes don't.
Choose the question with be. | Does she is ready? | Do she ready? | Is she ready? | 2 | Be questions invert is and the subject.
Which asks about a routine? | Do you walk to work? | Are you walking right now? | Did you walk yesterday? | 0 | Present simple is used for routines.""",
"Interview a partner about four routines and write short answers using do, does, don't and doesn't."),
unit("b18", "Sequencing instructions", "A2", "discourse", "Give a clear ordered process with imperatives and sequence words.",
"Instructions use a base verb: Open the file. Select a folder. Sequence words show order: first, next, then, finally. Before and after express relative order. A clear instruction names the object and avoids ambiguous it. Negative instructions use don't: Don't close the window yet. A reason can explain a step without changing its order.",
"List actions before writing sentences. Put one main action in each step. First creates the starting point; finally marks the last step. Replace unclear it with the file or folder name.",
"""Which starts a process? | First | Finally only | Yesterday only | 0 | First marks the initial step.
Which marks the last step? | Next always | Finally | Because only | 1 | Finally marks the conclusion.
Choose an imperative. | The file is open. | I opened it. | Open the file. | 2 | The base verb begins the instruction.
Don't close it yet means: | keep it open for now | close it immediately | it never existed | 0 | Don't prohibits the action at this point.
If it could refer to two files, use: | another unclear it | the specific file name | no object anywhere | 1 | Specific reference prevents confusion.
Do A before B means: | B must precede A | they must be simultaneous | A precedes B | 2 | Before establishes the sequence.
What helps a beginner follow a process? | clear objects and ordered steps | random ordering | removing every action | 0 | Explicit sequence and reference support execution.""",
"Write six steps for a simple computer task or recipe, including a negative instruction and a reason."),
unit("b19", "Zero conditional and general patterns", "A2", "grammar", "Describe a general relationship rather than one future prediction.",
"A zero conditional often uses if + present simple, present simple to describe general patterns: If water freezes, it becomes ice. It can also describe a routine response: If I'm late, I call. A first conditional concerns a particular future possibility: If I'm late tomorrow, I'll call. The difference depends on intended meaning, not the word if alone.",
"Ask general or particular future? A usual response → present in both clauses. One possible event tomorrow → present condition and will result. Do not put will into every condition automatically.",
"""General pattern: If water freezes, it ___ ice. | becomes | will became | becoming | 0 | Present simple describes the general relationship.
Which describes a routine response? | If I'm late tomorrow, I'll call. | If I'm late, I call. | If I had been late, I would have called. | 1 | Present forms describe the habitual response.
Which concerns a particular future possibility? | If I press this, it usually opens. | If I'm tired, I rest. | If it rains tomorrow, we'll stay home. | 2 | Tomorrow and will locate the possible future event.
The zero conditional often uses: | present simple in both clauses | past perfect in both | future perfect in every clause | 0 | This is its common general-pattern form.
What determines the intended conditional meaning? | the spelling of if alone | context and time reference | the number of commas only | 1 | Form and context work together.
Choose a general statement. | If I see Jo tomorrow, I'll ask. | If I had known, I'd have called. | If people skip practice, they often forget. | 2 | The sentence states a general tendency.
Is every general pattern an absolute scientific law? | No, some describe tendencies or routines. | Yes, always | Only if no comma appears | 0 | A general pattern can be habitual rather than exceptionless.""",
"Write three general routines and three particular future possibilities, clearly distinguishing their meaning."),
unit("b20", "Word families and spelling changes", "A2", "vocabulary", "Recognise basic related forms without assuming every word follows one rule.",
"A word family contains related forms: teach/teacher, help/helpful, happy/unhappy. -er can name a person who does an activity, -ful can form an adjective and un- can form an opposite. Spelling may change: happy → happiness. These patterns are useful clues, not rules that work for every word. Check unfamiliar forms in a dictionary.",
"First identify the role needed: person, quality or opposite. Teach → teacher; help → helpful; happy → unhappy. Do not create a form solely because a suffix worked with a different word.",
"""A person who teaches is a: | teacher | teachful | unteach only | 0 | Teacher is the conventional person noun.
The opposite of happy is often: | happyful | unhappy | teacher | 1 | Un- forms the opposite here.
Choose the adjective related to help. | helper only | helpingness | helpful | 2 | Helpful describes someone or something providing help.
Choose the standard spelling. | happiness | happyness | happyiness | 0 | Happy changes y to i in happiness.
Do these patterns work with every word? | Yes, without exception | No, verify unfamiliar forms | Only with capitals | 1 | Word formation has restrictions and exceptions.
Which is a person noun? | helpful | unhappy | worker | 2 | Worker names someone who works.
What can an affix provide? | a clue to word class or meaning | a guarantee of every meaning | the speaker's age | 0 | Affixes help interpretation but need context.""",
"Build a small dictionary of five word families, checking spelling and using each form in a sentence."),
],
"intermediate": [
unit("i17", "Question tags and checking assumptions", "B1", "interaction", "Check a proposition with an auxiliary-based tag.",
"A common tag pairs a positive statement with a negative tag: You're ready, aren't you? A negative statement takes a positive tag: She hasn't left, has she? Reuse the auxiliary, or use do/does/did for simple verbs. Intonation affects whether the speaker seeks real confirmation or expects agreement; a written exercise cannot assess that sound distinction.",
"Find polarity and auxiliary: has left → hasn't she? Hasn't left → has she? Works → doesn't he/she? Then practise rising and falling intonation with a speaker rather than inferring it from punctuation alone.",
"""You're ready, ___? | aren't you | don't you | isn't you | 0 | Reuse are with opposite polarity.
She hasn't left, ___? | hasn't she | has she | does she | 1 | A negative statement usually takes a positive tag.
He works here, ___? | isn't he | does he | doesn't he | 2 | Simple present work uses does in the tag.
They called, ___? | didn't they | aren't they | haven't they always | 0 | Simple past uses did.
Which aspect cannot a silent written tag fully assess? | auxiliary spelling | intonation | pronoun choice | 1 | Intonation is a property of speech.
She can swim, ___? | doesn't she | isn't she | can't she | 2 | Repeat can with opposite polarity.
A typical purpose of a tag is: | checking an assumption | naming an object only | forming a plural | 0 | Tags invite confirmation or agreement.""",
"Write five checking exchanges and practise two with rising and falling intonation with a partner."),
unit("i18", "Used to and being used to", "B1", "grammar", "Distinguish a past habit from familiarity.",
"Used to + base verb describes a past habit or state no longer presented as current: I used to live here. Be used to + noun/-ing means be familiar with: I'm used to working early. Get used to describes becoming familiar: I'm getting used to the schedule. In the familiarity expressions, to is a preposition, so an action takes -ing.",
"Test the meaning with two paraphrases: happened before → used to work. Familiar now → am used to working. Becoming familiar → am getting used to working. The same words do not have the same grammatical role in all three.",
"""Past habit: I ___ walk to school. | used to | am used to | get used to | 0 | Used to + base verb describes the past habit.
Familiar with early work: I'm used to ___ early. | work | working | worked to | 1 | To is a preposition in be used to.
Becoming familiar: I'm ___ the new timetable. | used lived | use to get | getting used to | 2 | Get used to describes the adaptation process.
'I used to live here' presents: | a past state | familiarity with houses only | a future booking | 0 | Used to can refer to an earlier state.
Choose the familiarity expression. | I used to work there. | I'm used to the noise. | I will work there. | 1 | Be used to means be accustomed to.
Why working after be used to? | all verbs always use ing | working is always a future tense | to is a preposition here | 2 | A preposition can take an -ing complement.
Which describes ongoing adaptation? | I'm getting used to driving on the left. | I used to drive here in 2010. | I drove yesterday. | 0 | Getting used to highlights becoming familiar.""",
"Compare an old routine, something familiar now and something you are still adapting to."),
unit("i19", "Practical emails: request, apology and action", "B1", "writing", "Write a purposeful email with the relevant context and next step.",
"A practical email should make its purpose clear early. Give enough context, a specific request or apology, and a useful next action. 'I'm sorry I missed our meeting. Could we reschedule for Tuesday at ten?' is clearer than a long message without a proposal. Match greeting and closing to the relationship; politeness does not require vague wording.",
"Use a four-part outline: purpose, relevant context, specific action, courteous closing. For an apology, state what happened without hiding it and offer a realistic repair. Remove unrelated background.",
"""Which request is most actionable? | Could we meet Tuesday at ten? | We should do something someday. | Meetings exist. | 0 | It proposes a specific action and time.
Where should the purpose normally become clear? | only after the closing | early in the message | nowhere explicitly | 1 | Early purpose helps the reader respond.
A useful apology often includes: | unrelated advertising | no reference to the problem | acknowledgement and a realistic repair | 2 | It recognises the issue and proposes a response.
Which background belongs in a rescheduling email? | the meeting being changed | every childhood memory | unrelated weather history | 0 | Context should support the action.
Politeness requires: | always being vague | suitable tone and a clear request | hiding the date | 1 | Clarity and courtesy are compatible.
Choose the clearer purpose sentence. | I write many things. | Some events happened. | I'm writing to request a later appointment. | 2 | It names the requested action.
Greeting and closing should reflect: | the relationship and situation | only the longest words available | a random style | 0 | Register depends on audience and purpose.""",
"Write an email apologising for a missed appointment and proposing two specific alternatives."),
unit("i20", "Prefixes, suffixes and dictionary use", "B1", "vocabulary", "Infer word class and check a plausible derived form.",
"Common patterns include -tion/-ment for many nouns, -able for some adjectives, and re- for repetition: revision, improvement, readable, rewrite. An affix gives a clue, not a guaranteed definition. In a dictionary, check word class, pronunciation, countability, complement pattern and example use. A translation alone may not show how to build a sentence.",
"Start from the sentence slot: after an article you may need a noun; before a noun you may need an adjective. Predict, then verify the whole form and use. Improvement is a noun; improve is a verb.",
"""Which is a noun related to improve? | improvement | improveablely | reimproven | 0 | Improvement is a conventional noun.
Readable is usually: | a preposition | an adjective | an auxiliary | 1 | Readable describes something that can be read with ease.
Rewrite usually means: | delete all language | read silently only | write again or revise | 2 | Re- commonly marks repetition.
Which should be checked beyond translation? | word class and example use | only font size | only alphabetical position | 0 | Grammar and context guide correct use.
An affix provides: | a guarantee in every word | a possible clue needing verification | no information ever | 1 | Patterns are useful but not universal.
Choose the noun after the article. | an improve | an improvingly | an improvement | 2 | The article precedes a suitable noun.
Why check countability? | It affects articles and plural forms. | It determines the writer's age. | It removes the need for context. | 0 | Noun grammar depends partly on countability.""",
"Select six new words from a text. Record word class, one related form, pronunciation information and an original sentence."),
],
"upper": [
unit("u17", "Causative have and get", "B2", "grammar", "Describe arranging a service without implying you performed it yourself.",
"Have/get + object + past participle can describe arranging a service: I had my bike repaired. This does not normally mean I repaired it myself. Compare I repaired my bike. The same construction can also describe an unwanted experience: She had her bag stolen. Context determines whether arrangement or experience is intended.",
"Separate the affected object from the performer. Had the bike repaired → someone repaired the bike for me. Had a bag stolen → an unwanted experience, not an arrangement to steal it.",
"""I had my bike repaired usually means: | I arranged for someone to repair it. | I necessarily repaired it myself. | I bought a new bike only. | 0 | The causative service reading separates arranger and performer.
Choose the complete service construction. | had repaired my | had my coat cleaned | had my coat clean to | 1 | Have + object + participle.
She had her bag stolen describes most naturally: | a planned cleaning service | a gift exchange | an unwanted experience | 2 | Context gives an adverse-experience reading.
Which explicitly says the speaker performed the repair? | I repaired my bike. | I had my bike repaired. | I got my bike repaired. | 0 | The active subject carries out the repair.
The verb after the object is normally: | a to-infinitive | a past participle | an arbitrary plural noun | 1 | Repaired/cleaned are participles.
Does have something done always mean a voluntary service? | Yes | Only with bags | No, context can indicate an unwanted experience. | 2 | The construction has more than one use.
Choose a service example. | We got the windows cleaned. | We got clean the windows to. | We got the windows cleaningly. | 0 | Object + cleaned forms the service causative.""",
"Describe three services you might arrange and distinguish one from an action you would do yourself."),
unit("u18", "Gradability and intensifiers", "B2", "vocabulary", "Choose natural combinations of degree words and adjectives.",
"Gradable adjectives such as tired allow degrees: very tired, slightly tired. Extreme or endpoint meanings often prefer other intensifiers: absolutely exhausted, completely full. These are tendencies with contextual flexibility, not a ban on creative usage. Quite can vary by adjective and variety of English, so infer strength from context rather than assuming it always means very.",
"Identify the scale. Tired allows small to large degrees. Exhausted often signals an extreme. Learn the conventional partnership: very tired, absolutely exhausted. Check quite in the actual context.",
"""Choose the conventional gradable phrase. | very tired | completely taller than absolutely | slightly impossible always | 0 | Very commonly intensifies a gradable adjective.
Choose the conventional extreme phrase. | very exhausted always only | absolutely exhausted | fairly absolutely tiringly | 1 | Absolutely naturally intensifies exhausted.
Completely full presents: | an unrelated colour | a time reference | an endpoint on a capacity scale | 2 | Full can be treated as a scale endpoint.
Are these combinations absolute bans on all creative usage? | No, context and usage matter. | Yes, in every context | Only nouns have flexibility. | 0 | Natural collocations are tendencies rather than universal logical laws.
Quite should be interpreted using: | only its first letter | adjective, variety and context | a fixed meaning of very in every case | 1 | Its force can vary.
Which weakens a gradable adjective? | absolutely only | completely only | slightly | 2 | Slightly marks a small degree.
The most useful learning unit is often: | an adjective-intensifier partnership in context | the adjective without any use | a random synonym list only | 0 | Conventional combinations support natural production.""",
"Describe contrasting experiences using six adjective-intensifier combinations and justify the degree of each."),
unit("u19", "Determiners: each, every, either and neither", "B2", "grammar", "Express distribution and choices without changing number or scope accidentally.",
"Each emphasises individual members; every looks across a whole set. Both normally precede a singular countable noun: each student, every student. Either refers to one of two alternatives; neither excludes both. Both refers to the two together. Compare neither option works with not every option works: the latter may leave some working options.",
"Draw the set. Two alternatives: both includes two, either can select one, neither selects zero. For a larger set, each/every + singular noun distributes a statement across members.",
"""Choose the standard noun phrase. | each student | each students | every students | 0 | Each takes a singular countable noun here.
Neither of two options means: | both | not one and not the other | only the first | 1 | Neither excludes both alternatives.
Both options means: | zero options | a single unspecified option | the two options together | 2 | Both includes the pair.
Choose the standard sentence. | Every student has a copy. | Every students have a copy. | Every student have a copies. | 0 | Every student is singular.
Not every option works means: | no option works necessarily | at least one does not work | every option works | 1 | It denies universal success, not all success.
Either option is acceptable means: | both are prohibited | neither exists | one or the other can be chosen | 2 | Either offers the two alternatives individually.
Which foregrounds individual distribution? | each | no article always | yesterday | 0 | Each attends to individual members.""",
"Write selection rules for a workshop using each, every, both, either and neither; explain the scope of every rule."),
unit("u20", "Past criticism and unnecessary action", "B2", "function", "Distinguish a missed better action from an unnecessary completed action.",
"Should have + participle can criticise or regret a past action not taken: You should have checked. Shouldn't have suggests the completed action was inadvisable. Needn't have + participle says an action happened but was unnecessary: You needn't have printed it. Didn't need to only states lack of necessity; without further context it does not always establish whether the action happened.",
"Separate what happened from what was required. Needn't have printed → printing happened and was unnecessary. Should have checked → checking was the better action. Don't infer a completed action from didn't need to without context.",
"""You should have checked commonly suggests: | checking was the better past action | checking is forbidden tomorrow | the action is a routine timetable | 0 | It evaluates the unrealised or inadequate past action.
You needn't have printed it entails normally that: | you did not print it | you printed it unnecessarily | printing was compulsory | 1 | Needn't have describes an unnecessary completed action.
You shouldn't have shouted suggests shouting was: | compulsory | a future prediction | inadvisable | 2 | It negatively evaluates the past action.
Choose the correct participle. | should have gone | should have went | should have go | 0 | Gone is the required participle.
Didn't need to, without more context, establishes: | a completed action in every case | lack of necessity | a guarantee of non-action in every case | 1 | Whether it happened can require context.
Which explicitly describes unnecessary completed work? | You must work now. | You should work tomorrow. | You needn't have rewritten the whole report. | 2 | The perfect modal marks a completed unnecessary action.
What should an accurate interpretation separate? | whether an action happened and whether it was necessary | tense from every context | only the spelling of have | 0 | Factual occurrence and necessity are different dimensions.""",
"Write a tactful project debrief distinguishing missed precautions, an inadvisable action and unnecessary work."),
],
"advanced": [
unit("a17", "Mandative subjunctive and formal recommendations", "C1", "grammar", "Recognise formal base-form clauses after a demand or recommendation.",
"In a mandative construction, some varieties use a base-form verb after that: They recommended that she be appointed; It is essential that he attend. The form does not add -s for he/she. A should construction is also common, especially in British usage: recommended that she should be appointed. Do not confuse this base form with an ordinary factual report.",
"Identify whether the clause expresses a requirement or a fact. Requirement: essential that he attend. Fact: he attends. For passive requirements use be + participle: that she be appointed.",
"""Choose a formal mandative form. | It is essential that he attend. | It is essential that he attending. | It essential he attended always. | 0 | The mandative subjunctive uses a base form.
They recommended that she ___ appointed. | is being always only | be | being | 1 | Passive mandative uses be + participle.
An alternative common in British usage is: | should appointed | should be appoint | should be appointed | 2 | Should + be + participle preserves the recommendation.
The clause here expresses: | a requirement or recommendation | necessarily an already completed fact | a colour | 0 | Mandative meaning concerns what should happen.
Does attend add -s after he in this construction? | Always | No, the base form is used. | Only in passive clauses | 1 | The subjunctive base form is uninflected.
Which is an ordinary factual report? | They insisted that he be present. | It is vital that he be present. | He attends every meeting. | 2 | Attends reports a habitual fact.
What should guide interpretation? | The governing expression and intended meaning | A claim that all that-clauses are subjunctive | Sentence length alone | 0 | The mandative construction is licensed by its context.""",
"Draft a formal recommendation with three requirements, then paraphrase each as a plain-language instruction."),
unit("a18", "C2: presupposition and loaded questions", "C2", "pragmatics", "Identify background assumptions without accepting them as established facts.",
"'When did the team stop ignoring complaints?' presents an earlier pattern of ignoring complaints as background. Answering only with a date may accept that premise. A careful response can contest it: 'That assumes complaints were ignored; what evidence supports that?' Similarly, 'Even Jo supported the proposal' can suggest Jo was an unlikely supporter, while 'Jo also supported it' presupposes another relevant supporter. Presuppositions often survive negation: 'Jo hasn't stopped commuting' still suggests prior commuting. In real discourse, context can cancel or challenge these readings. Distinguish what a sentence asserts from what it invites the listener to take for granted.",
"Make two lists: foreground assertion and background assumption. For a loaded question, write the assumed earlier state explicitly. Respond to an unsupported premise before answering within its frame.",
"""The question about stopping ignoring complaints backgrounds the idea that: | complaints had been ignored | every complaint was resolved | no team existed | 0 | Stop presents a preceding state as background.
Which response challenges the premise? | Last Tuesday. | That assumes complaints were ignored; what supports that? | At noon, certainly. | 1 | It addresses the unsupported background instead of accepting the frame.
Even Jo supported it can imply that Jo was: | the only possible supporter necessarily | definitely the chair | a comparatively unlikely supporter | 2 | Even evokes an expectation or scale.
Jo also supported it normally backgrounds: | another relevant supporter | that Jo opposed it | that the proposal was withdrawn | 0 | Also is additive.
What may survive negation in 'hasn't stopped commuting'? | only the date | the suggestion of earlier commuting | a guarantee of never commuting | 1 | The earlier activity remains backgrounded.
Does a presupposed claim become proven simply because it is backgrounded? | Yes | Only in questions | No | 2 | Linguistic packaging does not establish evidential truth.
A careful analyst separates: | assertion, background assumptions and contextual support | punctuation from all interpretation | every claim from every speaker | 0 | This prevents treating a loaded premise as verified evidence.""",
"Analyse five fictional interview questions for hidden assumptions, then rewrite them neutrally and explain what changed."),
unit("a19", "C2: necessity, sufficiency and exact paraphrase", "C2", "reading", "Preserve logical commitments when reformulating complex conditions.",
"'Access is granted only if registration is complete' makes registration necessary; it does not guarantee access whenever registration is complete. 'If registration is complete, access is granted' makes it sufficient in the stated rule. 'Unless approval is withheld, the trial proceeds' sets an exception, but context may determine how the approval process operates. Precise paraphrase preserves direction, scope, exceptions and degree of certainty. Reversing an implication is a common way to strengthen a source accidentally. Before summarising a dense condition, identify what is required, what guarantees an outcome, and what the text leaves unstated.",
"Draw an arrow for if: condition → result. Only if reverses the direction relative to the surface order: access → registration. Ask whether another requirement could still block access. Do not add a guarantee the wording never made.",
"""Access only if registration is complete makes registration: | necessary for access | sufficient by itself in every case | irrelevant | 0 | Only if marks a necessary condition.
If registration is complete, access is granted presents registration as: | impossible | sufficient under the stated rule | an unrelated observation | 1 | The condition leads to the result.
Does a necessary condition alone guarantee the outcome? | Yes, always | Only when written first | No | 2 | Other requirements may still be necessary.
Which preserves 'access only if registered'? | No unregistered person is granted access. | Every registered person is guaranteed access. | Registration never matters. | 0 | It preserves necessity without adding sufficiency.
An exact paraphrase should retain: | only word count | direction, scope and exceptions | only the topic noun | 1 | These determine the logical commitment.
What error reverses an implication? | preserving a limitation | naming the source | treating the result as a sufficient condition for the original cause | 2 | Reversal changes the rule's commitment.
Before strengthening a conditional claim, ask: | Does the source actually guarantee this direction? | Can I omit every exception? | Is a stronger statement more exciting? | 0 | Evidence and wording constrain a faithful paraphrase.""",
"Write four fictional access rules with if, only if and unless. Paraphrase them and give a counterexample to an incorrect reversal."),
unit("a20", "C2: self-repair and calibrated disagreement", "C2", "interaction", "Revise a spoken claim while maintaining coherence and interpersonal purpose.",
"Fluent communication includes monitoring and repair, not only uninterrupted speed. A speaker may say, 'The policy failed—more precisely, it missed the cost target while improving access.' The repair narrows an overgeneralisation without abandoning the main line. In disagreement, 'I accept the access gain; my reservation concerns the cost measure' separates agreement from the contested inference. A well-managed turn signals its purpose, acknowledges a relevant point and returns to the question. Excessive hedging can obscure commitment; categorical certainty can misrepresent evidence. Practise this in real timed interaction: reading a written dialogue cannot demonstrate spontaneous C2 spoken competence.",
"Underline the overbroad term failed. Replace it with a specific dimension: missed the cost target. Retain the concession: improved access. Then state the remaining disagreement and the evidence needed to resolve it.",
"""The repair after 'failed' primarily: | narrows an overgeneralisation | withdraws every observation | proves universal failure | 0 | It replaces a broad verdict with a dimension-specific account.
'My reservation concerns the cost measure' identifies: | agreement on every claim | the precise point of disagreement | the speaker's age | 1 | It targets a specific issue.
Does a written dialogue establish spontaneous spoken C2 ability? | Yes, entirely | Only if it is long | No | 2 | Actual interaction and expert assessment are needed.
An effective repair should: | correct the claim and reconnect with the main point | introduce an unrelated topic | hide every commitment | 0 | Repair supports accuracy and coherence.
Excessive hedging risks: | always improving clarity | obscuring the speaker's commitment | proving the evidence | 1 | Too many qualifications can blur the position.
Which acknowledges a gain while retaining a concern? | Everything failed in every way. | There are no possible concerns. | Access improved; the unresolved issue is cost. | 2 | It separates dimensions of evaluation.
What is needed to practise this skill properly? | real responsive interaction with feedback | silent reading alone | memorising only the answer letters | 0 | Turn management and repair need spontaneous production.""",
"Hold a five-minute debate with a partner. Each speaker must narrow one overbroad claim, acknowledge a valid point and ask an evidence-focused follow-up. Review a recording together."),
],
}

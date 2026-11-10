"""Original B2 units: complex forms, lexical choice and discourse."""
from course_authoring import unit

UNITS = [
unit("u05", "Third conditional and past alternatives", "B2", "grammar", "Discuss an unreal past condition and its past consequence.",
"Use if + past perfect, would have + past participle for an unreal past cause and result: If I had left earlier, I would have caught the train. The implication is that I did not leave early enough and did not catch it. Could have may express an unreal possibility rather than a definite hypothetical result.",
"Label both clauses past. Cause: had left. Result: would have caught. If the result is now, use the mixed conditional instead: would be here now.",
"""If I had known, I ___ helped. | would have | will | would had | 0 | A past unreal result uses would have + participle.
If she ___ earlier, she would have caught the train. | leaves | had left | would leave | 1 | The condition takes past perfect.
'If I had studied, I would have passed' normally implies: | I passed. | I will study. | I did not study sufficiently and did not pass. | 2 | The clauses describe an unreal past alternative.
Choose the participle. | would have gone | would have went | would have go | 0 | Gone is the past participle.
Which has a past result? | I would be there now. | I would have arrived yesterday. | I will arrive tomorrow. | 1 | Would have arrived describes a hypothetical past result.
Could have in a past alternative can express: | an obligatory present fact | a future timetable | a possible unreal outcome | 2 | Could highlights possibility or ability.
Choose a third conditional. | If we had booked, we would have got seats. | If we book, we will get seats. | If we had booked, we would be seated now. | 0 | Both the cause and result are past.""",
"Describe a fictional past setback and two alternative decisions, avoiding blame and distinguishing certain from possible outcomes."),
unit("u06", "Wishes, regrets and unreal time", "B2", "grammar", "Express a present wish and a past regret.",
"Wish + past form can describe a present situation we want to change: I wish I knew the answer. Wish + past perfect expresses a past regret: I wish I had checked. Wish + would can express a desired change in behaviour: I wish they would stop shouting. It is not a general substitute for every wish about your own state.",
"Choose the time before the form. Present lack of knowledge → wish I knew. Earlier mistake → wish I had checked. Annoying behaviour we want changed → wish they would stop.",
"""I don't know the answer. I wish I ___. | knew | had know | will know always | 0 | A past form expresses the unreal present wish.
I regret not checking. I wish I ___ checked. | would | had | have | 1 | Past regret takes past perfect.
The neighbours keep shouting. I wish they ___ stop. | had | are | would | 2 | Would expresses a desired behavioural change.
Which is a past regret? | I wish I had saved the file. | I wish I were taller. | I wish I knew French. | 0 | Had saved refers to the earlier missed action.
Which refers to a present state? | I wish I had left yesterday. | I wish I were more patient. | I wish they had called last week. | 1 | Were patient concerns the current state.
Complete: If only I ___ listened yesterday! | listen | will | had | 2 | If only + past perfect expresses regret.
What should guide form choice? | The time and type of desired change | Always use would | Always use present simple | 0 | Present wishes and past regrets use different forms.""",
"Write one present wish, one past regret and one wish about repeated behaviour. Explain the real situation behind each."),
unit("u07", "Passive aspects and reporting structures", "B2", "grammar", "Choose passive forms for ongoing, completed and reported events.",
"Passive forms preserve aspect: is being repaired (in progress); has been repaired (completed with present relevance); will be repaired (future). Reporting passives distance a claim from the writer: It is believed that ...; She is believed to live abroad. These report a belief rather than establish its truth.",
"Keep the meaning of the active form. Someone is repairing it → it is being repaired. Someone has repaired it → it has been repaired. In a reporting passive, identify whose belief is being reported if context allows.",
"""Repairs are in progress: The bridge ___. | is being repaired | has repaired | is repair | 0 | Being + participle preserves the ongoing passive meaning.
Repairs are complete: The bridge ___. | has being repaired | has been repaired | has repairing | 1 | Has been repaired is perfect passive.
A future passive is: | will repaired | will been repair | will be repaired | 2 | Use will be + participle.
'It is believed that ...' marks: | a reported belief | a guaranteed fact | a command | 0 | Belief is reported, not proven.
Choose the correct ongoing passive. | The files are been checked. | The files are being checked. | The files being check. | 1 | Are being checked is present continuous passive.
'She is believed to live abroad' means: | her location is mathematically proved | she was ordered abroad | people believe she lives abroad | 2 | The structure attributes a belief.
Choose the grammatical perfect passive. | The work has been completed. | The work has being completed. | The work has complete. | 0 | Perfect passive is has been + participle.""",
"Write a short project update distinguishing work in progress, completed work, planned work and an unconfirmed reported claim."),
unit("u08", "Reported questions and instructions", "B2", "grammar", "Relay a question or instruction without direct-question word order.",
"Reported questions use statement word order: She asked where I lived, not where did I live. Yes/no questions use if or whether: He asked whether I was ready. Report instructions with tell/ask + object + to-infinitive: She told me to wait. For a negative instruction: told me not to leave.",
"Remove question inversion inside the report. Where do you live? → where I lived. Are you ready? → whether I was ready. Don't leave → told me not to leave.",
"""She asked where ___. | I lived | did I live | lived I | 0 | Use statement order in the reported question.
He asked ___ I was ready. | that whether | whether | what where | 1 | Whether introduces a reported yes/no question.
Report 'Wait here.' | She told that wait. | She told me waiting. | She told me to wait there. | 2 | Tell + object + to-infinitive reports an instruction.
Report 'Don't leave.' | He told me not to leave. | He told me to not left. | He said me leave not. | 0 | Not to leave is the negative infinitive.
Which preserves correct embedded order? | I wonder where is she. | I wonder where she is. | I wonder where she does is. | 1 | Embedded questions normally have statement order.
'Did you book?' can become: | He asked did I booked. | He asked that booking. | He asked if I had booked. | 2 | If introduces the question; backshift may use had booked.
Choose the complete instruction report. | They asked us to be quiet. | They asked to us quiet. | They said us to quiet. | 0 | Ask takes an object and a to-infinitive here.""",
"Report a conversation containing a location question, a yes/no question and two instructions."),
unit("u09", "Non-defining relatives and whose", "B2", "grammar", "Add supplementary information without changing reference.",
"Non-defining relatives add extra information and are normally separated by commas: My sister, who lives in York, is visiting. Do not normally use that in this construction. Whose marks possession: the student whose laptop broke. A defining clause identifies which person; a supplementary clause assumes the person is already identified.",
"Ask whether the information identifies the person or merely adds detail. Extra detail → commas and who/which, not that. Possession within a clause → whose + noun.",
"""Kim, ___ lives in York, is visiting. | who | that | where | 0 | Non-defining person relatives take who.
The student ___ laptop broke needs help. | who's | whose | which | 1 | Whose marks possession.
Non-defining clauses normally use: | no punctuation at all | that only | commas around supplementary information | 2 | Commas signal the added information.
Which is a defining clause? | The students who finished may leave. | Kim, who finished, left. | York, which is in England, is historic. | 0 | It identifies the relevant subset of students.
Whose differs from who's because who's means: | belonging to whom only | who is or who has | a relative place | 1 | The apostrophe marks a contraction.
Choose the supplementary thing-relative. | My car, that is old, broke. | My car, who is old, broke. | My car, which is old, broke. | 2 | Which is used for the thing in this non-defining clause.
'My brother, who lives abroad, called' presents living abroad as: | supplementary information | a question about a place | the object of called | 0 | The comma-marked clause adds information.""",
"Describe a person and an organisation using defining, non-defining and possessive relative clauses with deliberate punctuation."),
unit("u10", "Future perfect and future continuous", "B2", "grammar", "Distinguish completion before a future point from activity at that point.",
"Future perfect: will have + past participle, for completion by a future point: By Friday, I'll have finished. Future continuous: will be + -ing, for activity in progress at a future time: At six, I'll be travelling. By focuses on a latest completion point; at can locate an activity in progress.",
"Draw Friday as a point. Finished before or by it → will have finished. An action crossing six o'clock → will be travelling at six. Choose meaning before formula.",
"""By Friday, I ___ the report. (completed) | will have finished | will finishing | will have finish | 0 | Future perfect marks completion by then.
At six tomorrow, I ___ home. (in progress) | will have drive | will be driving | will been drove | 1 | Future continuous locates an ongoing action.
Which form requires a past participle? | will be + ing | present simple | will have + participle | 2 | Future perfect uses a participle.
'By noon' commonly sets: | a latest completion point | a permanent habit | the speaker's location | 0 | By sets the endpoint by which something is achieved.
Choose the correct form. | will have wrote | will have written | will have writing | 1 | Written is the past participle.
Which focuses on activity at a future time? | I finished yesterday. | I have finished now. | I'll be presenting at ten. | 2 | Will be presenting is future continuous.
Choose the completion claim. | By next month, we'll have moved. | Next month, we'll be moving all day. | We are moving now. | 0 | The perfect form places completion by next month.""",
"Write a future project timetable stating three expected completions and two activities in progress at specific times."),
unit("u11", "Stative verbs and changing meanings", "B2", "grammar", "Choose aspect according to meaning rather than a memorised verb ban.",
"Many state meanings prefer simple forms: I know; I own; I believe. Some verbs have different state and activity meanings. I think it's good = opinion; I'm thinking about it = active consideration. She has a car = possession; she's having lunch = activity. You're being rude describes temporary behaviour, not necessarily a permanent trait.",
"Ask what the verb means in this sentence. Think = opinion → simple. Think about = active mental activity → continuous is possible. Have = own → simple; have lunch → an activity.",
"""Opinion: I ___ this is useful. | think | am thinking always | thinking | 0 | Think as an opinion normally uses simple aspect.
Active consideration: I ___ about your offer. | knows | am thinking | own | 1 | Thinking about is a current activity.
Possession: She ___ a bicycle. | is having always | having | has | 2 | Have as possession normally takes simple aspect.
Activity now: She ___ lunch. | is having | is owning | has had every day now only | 0 | Having lunch is an activity.
'You're being rude' can describe: | a permanent definition only | current behaviour | a future possession | 1 | Being can present temporary behaviour.
Choose the usual state form. | I'm knowing the answer. | I knowing the answer. | I know the answer. | 2 | Know normally has a state meaning.
What determines the aspect here? | The verb's meaning in context | A rule that every verb takes ing | The number of letters | 0 | Different senses permit different aspect choices.""",
"Contrast think/think about, have/have lunch and be/being in six contextualised sentences."),
unit("u12", "Verb patterns that change meaning", "B2", "grammar", "Distinguish remembering an action from remembering to act.",
"Remember doing recalls an earlier experience; remember to do avoids forgetting a needed action. Stop doing ends that activity; stop to do interrupts another activity for a purpose. Try doing experiments with a method; try to do attempts a task. The form changes the relationship between events.",
"Put events on a timeline. Remember locking: locking first, memory later. Remember to lock: reminder first, locking afterwards. Stop talking: talking ends. Stop to talk: another activity pauses so talking can start.",
"""Please remember ___ the door before leaving. | to lock | locking yesterday only | locked | 0 | Remember to do concerns a required action.
I remember ___ the door yesterday. | to locking | locking | lock to | 1 | Remember doing recalls an experience.
She stopped smoking means: | she paused work to smoke | she started smoking | she ended the smoking habit | 2 | Stop doing ends that activity.
We stopped to buy water means: | we paused another activity in order to buy water | we never bought water again | buying water was forbidden | 0 | Stop to do introduces the purpose of the pause.
Try restarting it suggests: | never experiment | test restarting as a method | remember a past restart | 1 | Try doing can propose an experiment.
He tried to lift it but couldn't means: | he successfully lifted it repeatedly | he forgot lifting it | he attempted the task unsuccessfully | 2 | Try to do describes the attempt.
Why learn both forms? | They can express different event relationships. | They always mean exactly the same. | Only one exists in English. | 0 | The complement form can change the meaning.""",
"Write a troubleshooting dialogue using try doing, try to do, remember to do and stop doing with clear contexts."),
unit("u13", "Separable multiword verbs", "B2", "vocabulary", "Place objects correctly in common multiword verbs.",
"Some phrasal verbs allow a noun object before or after the particle: turn off the light / turn the light off. A pronoun object normally goes between: turn it off. Others are inseparable: look after the child / look after her, not look her after. Learn meaning and object pattern together.",
"Test the verb's pattern. Turn off is separable: turn the radio off; turn it off. Look after is inseparable: look after Sam; look after him. Pronoun placement reveals the difference.",
"""Replace the light with it: | Turn it off. | Turn off it. | Turn off of it. | 0 | A pronoun goes inside this separable phrasal verb.
Choose the inseparable pattern. | Look her after. | Look after her. | Look after of her. | 1 | Look after keeps its object after after.
Which is also grammatical? | Turn off it. | Turn the off light. | Turn the light off. | 2 | A noun object can separate turn and off.
Pick up the parcel → | Pick it up. | Pick up it. | Pick of it up. | 0 | Pronoun objects go between pick and up.
What should a dictionary entry help identify? | only spelling | meaning and object placement | only word length | 1 | Both meaning and syntax are needed.
Choose the correct childcare sentence. | She looks him after. | She after looks him. | She looks after him. | 2 | Look after is not separable in this meaning.
Which noun-object variant is correct? | Put your coat on. | Put on it. | Put your on coat. | 0 | Put on is separable with a noun object.""",
"Write instructions using turn off, pick up and put on, then replace each noun object with a pronoun."),
unit("u14", "Collocation, intensity and idioms", "B2", "vocabulary", "Select conventional partnerships and interpret an idiom in context.",
"Conventional combinations include heavy rain, strong evidence and deeply concerned. Not every synonym can replace each word naturally. An idiom may have a non-literal meaning: break the ice means ease initial social tension. Use context and register to decide whether an idiom fits; avoid filling formal reports with casual expressions.",
"Learn a whole phrase with its function. Heavy rain describes intensity. Strong evidence supports a claim. Break the ice is about beginning social interaction, not necessarily damaging frozen water.",
"""Choose the usual weather collocation. | heavy rain | weighty rain | powerful rain always | 0 | Heavy rain is the conventional phrase.
Choose the usual evidence phrase. | muscular evidence | strong evidence | loud evidence always | 1 | Strong evidence is conventional.
'A game helped break the ice' likely means: | the room froze | the floor broke | the game eased initial social tension | 2 | The social context signals the idiomatic sense.
Choose the natural phrase. | deeply concerned | deeply tall | heavily intelligent always | 0 | Deeply concerned is conventional.
When using an idiom, check: | only its letter count | meaning, context and register | whether every word is literal | 1 | Appropriate use depends on all three.
Which approach is useful? | Replace every word with any synonym. | Ignore context. | Record collocations with examples. | 2 | Examples preserve conventional partnerships.
Why might casual idioms be unsuitable in a formal report? | They can mismatch the expected register. | Formal English forbids all figurative language. | Idioms are always grammatical errors. | 0 | Suitability is a matter of audience and purpose.""",
"Write an informal welcome using one idiom, then rewrite it for a formal event without that idiom."),
unit("u15", "Reference, cohesion and linking", "B2", "discourse", "Make relationships and references clear across sentences.",
"Cohesion connects sentences through pronouns, repeated key terms and linkers. A pronoun needs an identifiable referent. However marks contrast; therefore marks a result or inference; moreover adds support. A linker cannot create a logical relationship that the ideas do not support. If this or it is ambiguous, name the concept explicitly.",
"For each pronoun, draw an arrow to its referent. For each linker, name its relationship. If an arrow could point to two things, replace the pronoun with a specific noun phrase.",
"""However normally signals: | contrast | identical repetition only | a greeting | 0 | However marks a contrasting idea.
Therefore normally signals: | an unrelated detail | a result or inference | a person's name | 1 | Therefore presents a consequence or inference.
An unclear it should often be replaced with: | more unclear pronouns | no punctuation anywhere | a specific noun phrase | 2 | Naming the referent can remove ambiguity.
Moreover generally adds: | further support or information | a prohibition | a past tense ending | 0 | Moreover is additive.
Can a linker fix an illogical argument by itself? | Always | No | Only if capitalised | 1 | The ideas must support the relationship.
What is a referent? | a word's font | the last punctuation mark | the person or idea a referring expression points to | 2 | Reference connects expressions to entities or concepts.
Which revision clarifies 'This was costly' after several possible causes? | The delay was costly. | It this was costly. | That it was costly. | 0 | The delay identifies the intended referent.""",
"Write a two-paragraph recommendation with contrast, consequence and clear pronoun reference; explain each link."),
unit("u16", "Reports, trends and cautious comparisons", "B2", "reading", "Describe figures without confusing levels, changes or causes.",
"A rise from 20 to 30 is an increase of 10 units, or 50% relative to 20. A rise from 20% to 30% is 10 percentage points. A trend describes a pattern over time; it does not by itself prove a cause. State units, period and comparison base. Separate an observed result from your interpretation.",
"Write starting value, ending value and unit. Subtract for absolute change; divide the difference by the starting value for relative change. For percentages as levels, distinguish percentage points from percent change.",
"""A rise from 20 units to 30 units is an increase of: | 10 units | 30 units | 50 units | 0 | 30 minus 20 equals 10.
Relative to 20, that increase is: | 10% | 50% | 150% | 1 | 10 divided by 20 is 50%.
20% to 30% is a rise of: | 10 percent relative | 30 percentage points | 10 percentage points | 2 | Subtract percentage levels for percentage points.
Does a trend alone prove a cause? | No | Yes | Only if drawn in blue | 0 | An observed pattern does not establish causation.
A clear comparison should state: | only the highest number | units, period and comparison base | only the author's opinion | 1 | These make the figures interpretable.
Which is an interpretation rather than a direct observation? | Sales rose from 20 to 30. | The measured increase was 10 units. | The campaign may have contributed to the rise. | 2 | May have contributed proposes an explanation.
Which wording preserves scope? | In this survey, 60% selected option A. | All people everywhere prefer A. | The survey proves every future choice. | 0 | In this survey limits the claim appropriately.""",
"Write a 150-word report on fictional figures, including an absolute change, relative change, limitation and cautious interpretation."),
]

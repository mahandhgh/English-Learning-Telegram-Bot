"""Original B1 units: connected narrative, forms and communication strategies."""
from course_authoring import unit

UNITS = [
unit("i05", "Past perfect and narrative sequence", "B1", "grammar", "Show which of two past events happened first.",
"The past perfect uses had + past participle to place an event before another past reference point: When I arrived, the train had left. Leaving happened before arrival. Use past simple for the main sequence of a narrative. Past perfect is useful when the order needs clarification, not for every past event.",
"Draw two points: train leaves, then I arrive. Mark the earlier point had left and the later one arrived. Once the timeline is clear, a story can continue in past simple.",
"""When I arrived, the train had left. Which happened first? | The train left. | I arrived. | Both necessarily happened together. | 0 | Had left places leaving before arrival.
She realised she ___ her wallet at home. | leaves | had left | has leave | 1 | Had left is the earlier event in this past narrative.
Choose the past perfect form. | has went | had go | had gone | 2 | Use had + past participle gone.
Which normally tells the main sequence? | Past simple | Present perfect only | Future perfect only | 0 | Past simple commonly carries the main narrative sequence.
We couldn't enter because we ___ our tickets. | forget now | had forgotten | will forget | 1 | The forgetting precedes the failed entry.
Had studied means: | an event after a future moment | a routine now | studying before a past reference point | 2 | Had + participle marks the earlier past.
Must every verb in a past story be past perfect? | No, use it to clarify an earlier past. | Yes, always | Only negatives use it. | 0 | Past perfect has a specific sequencing function.""",
"Tell a short story about a missed appointment, distinguishing an earlier mistake from the main events."),
unit("i06", "Present perfect continuous", "B1", "grammar", "Connect a continuing or recent activity with the present.",
"Use have/has been + -ing for an activity continuing up to now or explaining a present result: I've been studying for two hours. She's tired because she's been running. Contrast a completed count: I've read three chapters. Stative verbs such as know normally use present perfect simple: I've known her for years.",
"Ask activity or completed result? Activity duration → have been reading. Completed number → have read three chapters. Know is a state, so use have known, not have been knowing.",
"""I ___ for two hours and I'm still working. | have been studying | studied tomorrow | have study | 0 | The form highlights a continuing activity.
She ___ three reports so far. (completed count) | has been write | has written | writing | 1 | Use simple perfect for the completed number.
Choose the usual state form. | I've been knowing Jo. | I knowing Jo. | I've known Jo for years. | 2 | Know normally takes the simple form.
Her shoes are muddy because she ___ in the garden. | has been working | has work | have working | 0 | The recent activity explains the present result.
Complete: He has ___ waiting. | be | been | being have | 1 | Perfect continuous uses has been + -ing.
Which focuses on an activity's duration? | I've finished two books. | I finished yesterday. | I've been reading all afternoon. | 2 | All afternoon with the continuous focuses on duration.
Which is a duration expression? | for three hours | yesterday at noon only | in 2010 only | 0 | For introduces a period of time.""",
"Describe one activity continuing up to now and one completed result, making the distinction explicit."),
unit("i07", "Predictions and future clauses", "B1", "grammar", "Make predictions and use time clauses for future events.",
"Will often introduces a prediction or belief: I think it will rain. Going to can highlight present evidence: Look at those clouds; it's going to rain. After when, as soon as and until in future time clauses, normally use a present form: I'll call when I arrive. Do not automatically put will in both clauses.",
"Separate main future clause from time clause. Main: I'll call. Time: when I arrive. With visible evidence, going to makes the link to what you can see explicit.",
"""I'll call when I ___. | arrive | will arrive | arrived yesterday | 0 | A future time clause normally uses present simple.
Look at those dark clouds. It ___ rain. | going | is going to | gone to | 1 | Going to can link a prediction to current evidence.
As soon as she arrives, we ___ dinner. | started yesterday | starting | will start | 2 | The main clause can use will.
Choose the standard time clause. | until the shop opens | until the shop will opens | until opens will | 0 | Use present simple after until for this future reference.
I think robots ___ change some jobs. | changing | will | were | 1 | Will expresses a prediction.
Which makes present evidence explicit? | It rained in 2010. | It rains often. | That glass is slipping; it's going to fall. | 2 | The slipping glass supports the prediction.
Choose the correct sentence. | We'll leave after Jo finishes. | We'll leave after Jo will finishes. | We'll leave after finishes Jo will. | 0 | After introduces a present-form future time clause.""",
"Describe three future expectations and a plan with when, until or as soon as."),
unit("i08", "Passive voice and processes", "B1", "grammar", "Describe a process with attention on the affected thing.",
"The passive uses be + past participle: The parcels are checked. The parcel was delivered. It focuses on what happens to the subject, often when the agent is unknown or unimportant. Add by to name an agent: The novel was written by Kim. Keep the tense in be; the participle does not change.",
"Active: Workers check parcels. Passive: Parcels are checked. Move the affected thing to subject position, choose be for the time and number, then add the participle.",
"""The parcels ___ checked every morning. | are | is | was | 0 | Present plural passive uses are checked.
The parcel ___ delivered yesterday. | is being tomorrow | was | were | 1 | Singular past passive uses was delivered.
Name an agent: The book was written ___ Kim. | from | with always | by | 2 | By introduces the agent.
Which is passive? | The windows were cleaned. | They cleaned the windows. | They clean windows. | 0 | Were + cleaned is passive.
The passive focuses here on: | who is tallest | what happens to the subject | the speaker's age | 1 | It foregrounds the affected subject.
Choose the correct form. | was wrote | were write | was written | 2 | Written is the past participle.
In 'The bridge was built in 1990', the stated time is: | the time of building | necessarily the time of speaking | a future deadline | 0 | Was built locates construction in the past.""",
"Describe how a product is made or delivered using four passive sentences."),
unit("i09", "Defining relative clauses", "B1", "grammar", "Identify a person, thing or place with a relative clause.",
"A defining relative clause tells us which one: the person who called; the book that I bought; the cafe where we met. Use who for people, which/that for things and where for places. An object relative pronoun can often be omitted: the book I bought. A subject relative pronoun cannot simply be removed.",
"Find the clause's missing role. The person ___ called: the missing word is the subject, so keep who. The book ___ I bought: I is already the subject, so the object relative can be omitted.",
"""The person ___ called is my tutor. | who | where | when | 0 | Who refers to a person and is the clause subject.
The cafe ___ we met is closed. | who | where | whose always | 1 | Where introduces the place relationship.
Which object relative can be omitted? | The person who called | The car that broke down | The book that I bought | 2 | In I bought, I is the subject and that is the object.
Choose the defining clause. | The student who lives next door | The student is tall. | Hello, student. | 0 | It identifies which student.
The machine ___ makes coffee is broken. | where | that | when | 1 | That refers to the thing and is the relative subject.
Choose the grammatical sentence. | The woman lives next door called. (intended relative) | The woman where called lives here. | The woman who called lives here. | 2 | Keep a subject relative pronoun.
'The bag I lost' means: | the bag that I lost | the person who lost me | every bag everywhere | 0 | The object relative that is omitted.""",
"Describe three people, two objects and one place so a reader can identify each."),
unit("i10", "Modal meanings: permission and possibility", "B1", "function", "Distinguish permission, ability and uncertainty using context.",
"Can may express ability or permission: She can swim; You can leave now. May/might can express possibility: The train might be late. Could can be a polite request or a possibility. Read the context to identify the function rather than assigning each modal one fixed meaning. A modal normally takes a base verb.",
"Label the sentence's purpose before choosing a modal: skill → ability; allowed action → permission; uncertain event → possibility; asking someone to act → request.",
"""'You can leave now; the meeting is over' gives: | permission | past deduction | a count | 0 | The context allows leaving.
'She can swim well' expresses: | prohibition | ability | certainty about the past | 1 | Swimming skill is an ability.
'It might snow' expresses: | a requirement | a guarantee | a possibility | 2 | Might marks uncertainty.
Which is a polite request? | Could you check this? | It could rain. | She could swim at six. | 0 | Could you requests action.
Choose the complete form. | It might rains. | It might rain. | It might raining. | 1 | A modal takes the base verb rain.
Does might mean certain? | Yes, always | It means forbidden | No, it signals possibility. | 2 | Might leaves the outcome uncertain.
Which shows that context matters? | Can can express ability or permission. | Can always means the same thing. | Modals never depend on purpose. | 0 | Modal meanings vary with context.""",
"Write four sentences using can, could and might; label the intended function of each."),
unit("i11", "Enough, too, a little and a few", "B1", "grammar", "Express sufficiency, excess and small quantities precisely.",
"Too means more than desirable: too hot. Enough means sufficient: warm enough, enough money. Put enough after an adjective but before a noun. A few goes with countable plurals; a little with uncountable nouns. Without a, few/little often highlight a shortage: few seats remain; little time is left.",
"Name the noun type first: seats → a few; time → a little. Decide whether there is sufficient quantity: enough time. With a quality, put enough last: clear enough.",
"""We have ___ time to finish. (sufficient) | enough | too many | few | 0 | Enough before time means sufficient time.
The explanation is clear ___. | too | enough | a few | 1 | Enough follows the adjective.
A small positive quantity of chairs: | a little chairs | much chairs | a few chairs | 2 | Chairs is countable and plural.
A small positive quantity of water: | a little water | a few water | many water | 0 | Water is uncountable.
'Too hot to drink' means: | the ideal temperature | hotter than is suitable for drinking | cold enough | 1 | Too signals an excessive degree.
'Few seats remain' normally emphasises: | plenty of space | a positive abundance | a shortage | 2 | Few without a has a negative orientation.
Choose the normal word order. | enough money | money enough always | enough expensive | 0 | Enough precedes a noun.""",
"Describe preparations for a trip using enough, too, a little and a few."),
unit("i12", "Common collocations and dependent prepositions", "B1", "vocabulary", "Learn frequent word partnerships as units.",
"A collocation is a conventional partnership: make a decision, do homework, take a break. Some words select a preposition: interested in, good at, depend on. Learn the whole chunk with an example rather than replacing its preposition through literal translation. Partnerships are usage patterns, not universal logical rules.",
"Store a phrase and one context: make a decision about a course; do homework after class; depend on the weather. Test the whole chunk, not an isolated word.",
"""We need to ___ a decision. | make | do | perform always | 0 | Make a decision is the conventional chunk.
I ___ my homework after dinner. | make | do | take | 1 | Do homework is standard.
Let's ___ a break. | make | do | take | 2 | Take a break is conventional.
She is interested ___ astronomy. | in | on | at | 0 | The phrase is interested in.
He is good ___ explaining ideas. | on | at | of | 1 | The phrase is good at.
It depends ___ the weather. | at | in | on | 2 | Depend normally takes on.
What is useful to record? | The whole phrase with a context | Only the word's first letter | An invented preposition | 0 | Context and the full chunk support appropriate use.""",
"Write a short study plan using make a decision, do homework, take a break and depend on."),
unit("i13", "Phrasal verbs in daily life", "B1", "vocabulary", "Understand common multiword verbs in context.",
"A phrasal verb combines a verb with a particle, sometimes with a meaning beyond the parts: give up = stop trying or stop an activity; look after = care for; find out = discover information. A word such as up does not have one meaning across every phrase. Use context and learn the whole verb.",
"Replace the chunk with a simple explanation: look after a child → care for a child. Find out the time → discover it. Keep a context so similar-looking phrases do not get mixed up.",
"""Who will look after the cat? means: | Who will care for it? | Who will look behind it? | Who will sell it? | 0 | Look after means care for.
I need to find out the time. means: | hide the time | discover the time | cancel the time | 1 | Find out means discover information.
Don't give up on your goal. means: | reach it immediately | forget every word | don't stop trying | 2 | Give up can mean stop trying.
Turn off the light means: | stop its operation | make it brighter necessarily | move it outdoors | 0 | Turn off stops operation.
Why learn a phrasal verb in context? | Every particle always means one thing. | Its meaning may not follow directly from the parts. | Context never matters. | 1 | Whole-phrase meaning can be idiomatic.
She picked up the bag from the floor. Here picked up means: | forgot | cancelled | lifted | 2 | The physical context indicates lifting.
Which is a multiword verb? | look after | quickly | beautiful | 0 | It combines a verb and another element.""",
"Write a day-in-the-life paragraph using five multiword verbs with enough context to show their meanings."),
unit("i14", "Opinion paragraphs and supporting reasons", "B1", "writing", "Build a focused paragraph with a reason and example.",
"A clear opinion paragraph usually states a point, explains a reason and gives relevant support. 'The town needs a later bus because evening classes finish after six. For example, students currently walk home in the dark.' A conclusion can connect the support back to the point. A new unrelated topic weakens focus.",
"Label each sentence: opinion → why → example → link back. Check that the example actually supports the reason. Remove an interesting sentence if it does not help the paragraph's central point.",
"""Which states an opinion? | The town should add a later bus. | The bus leaves at six. | The ticket costs two pounds. | 0 | Should add expresses a recommendation.
What does because introduce? | a greeting | a reason | a title only | 1 | Because explains why.
Which supports a later bus for students? | The mayor likes blue. | Apples are popular. | Evening classes finish after the final bus. | 2 | The fact explains the transport need.
For example usually introduces: | an illustration | a prohibition | a new unrelated topic necessarily | 0 | An example makes a point concrete.
What should a focused paragraph avoid? | relevant evidence | unrelated topic shifts | an explanation | 1 | Unrelated ideas weaken focus.
Which is a logical conclusion? | Therefore, cancel all classes without discussion. | Therefore, paint the apples. | Therefore, an evening service would improve access. | 2 | It links the evidence to the proposal.
Which order is useful? | point, reason, example | example, unrelated joke, new topic | random sentences only | 0 | The order helps the reader follow the argument.""",
"Write 100–130 words recommending one improvement to your town; include a reason, example and concluding link."),
unit("i15", "Clarifying and repairing a conversation", "B1", "interaction", "Ask for repetition, clarification and confirmation.",
"Communication includes repairing misunderstandings. Ask for repetition: Could you say that again? Ask for meaning: What do you mean by flexible? Confirm an interpretation: Do you mean Tuesday rather than Thursday? Rephrase your own point: What I mean is ... . Clarify the specific problem instead of pretending to understand.",
"Decide what went wrong. Sound missed → ask to repeat. Meaning unclear → ask what it means. Two possible interpretations → confirm one explicitly. Repairing a misunderstanding is a useful communication skill.",
"""You did not hear the last sentence. Say: | Could you say that again? | I fully agree. | Goodbye forever. | 0 | This requests repetition.
You do not understand flexible. Ask: | What colour is flexible? | What do you mean by flexible? | Who is yesterday? | 1 | This requests meaning clarification.
Confirm a date. | The meeting exists. | You are a meeting. | Do you mean Tuesday rather than Thursday? | 2 | It checks a specific interpretation.
Introduce a rephrasing. | What I mean is ... | It is forbidden to explain. | Never mind all meaning. | 0 | The phrase signals reformulation.
Why identify the specific misunderstanding? | To avoid ever listening | To make the repair useful | To change every subject | 1 | Specific clarification targets the actual problem.
Which is a confirmation check? | I know everything. | Don't repeat anything. | So we meet at six, correct? | 2 | It checks a shared understanding.
If you still do not understand, a useful response is: | Could you give an example? | Pretend agreement. | Invent the instructions. | 0 | An example can clarify the meaning.""",
"Write a dialogue where two people resolve a misunderstanding about a meeting date and location."),
unit("i16", "Stress, connected speech and listening strategies", "B1", "pronunciation", "Plan listening for gist, details and word boundaries.",
"In speech, important content words often carry prominence while function words may be reduced. Word boundaries may be less obvious than in writing. First listen for the situation and main point, then for names, numbers or contrasts. Do not stop at every unknown word. This lesson teaches a strategy; actual listening requires audio or a partner, not only a written script.",
"Use two passes. Pass one: who, where, why? Pass two: what time, which option, what changed? Ask a partner to read: 'The meeting isn't on Thursday; it's on Tuesday at six.' Listen without looking, then check the script.",
"""The first listening pass should usually focus on: | the main situation and point | every spelling detail | writing every word exactly | 0 | Gist gives a framework for details.
A second pass can focus on: | unrelated grammar only | times and changes | ignoring all numbers | 1 | Details become easier within the main context.
'Not Thursday, Tuesday' signals: | no date information | identical days | a correction or contrast | 2 | The contrast highlights the corrected day.
Does a written script alone assess listening comprehension? | No | Yes, completely | Only if printed in capitals | 0 | Reading a script is not listening to audio.
Which may be reduced in connected speech? | only proper names | function words | every stressed word equally | 1 | Many function words have weak forms.
When one word is unknown, a useful approach is: | abandon the whole message | invent every detail | continue and use context | 2 | Context can preserve overall comprehension.
How can you practise the script as listening? | Have someone read it while you do not look. | Read it silently only. | Count its letters only. | 0 | Audio input without the visible text practises listening.""",
"Ask a partner to read the meeting script twice without showing it. Note the corrected day and time, then check together."),
]

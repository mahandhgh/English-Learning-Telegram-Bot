"""Original supplementary content, not copied from any commercial course.

Each lesson has five practice questions and two checkpoint questions.
The first three questions of existing lessons keep their original indices.
"""

def expand(lessons, q, lesson):
    additions = {
        "s1": ("👋 Meet someone: Hello!\n🙂 Give your name: My name is Alex.\n👋 Leave: Goodbye!\nTry: Hello! My name is ___.", [
            q("Sam says 'Hi!' What is a good reply?", ["Hello!", "Three.", "Apple."], 0, "Hi and Hello are greetings."),
            q("Complete: My ___ is Alex.", ["goodbye", "name", "hello"], 1, "My name is Alex introduces Alex."),
            q("Which phrase introduces you?", ["Goodbye!", "Hi!", "My name is Kim."], 2, "My name is + your name introduces you."),
            q("Alex is leaving. Choose a reply.", ["Bye, Alex!", "My apple.", "Two."], 0, "Bye is a short form of Goodbye."),
        ]),
        "s2": ("Count each apple: 🍎 = 1 = one. 🍎🍎 = 2 = two. 🍎🍎🍎 = 3 = three.\nOne apple has no -s. Two apples and three apples have -s.", [
            q("🍎🍎🍎 Choose the number.", ["one", "three", "two"], 1, "Three apples: 3."),
            q("🍎 Choose the phrase.", ["one apples", "two apples", "one apple"], 2, "Use singular apple after one."),
            q("2 = ___", ["two", "one", "three"], 0, "The word for 2 is two."),
            q("Complete: three ___", ["apple", "apples", "one"], 1, "Three takes the plural apples."),
        ]),
        "b1": ("Find the subject first. With he/she/it, add -s or -ies: she reads; he studies.\nWith I/we/you/they, use the base verb: they read.\nFor a negative, doesn't already marks he/she/it: he doesn't read.", [
            q("My friends ___ in a cafe every Saturday.", ["meets", "meet", "meeting"], 1, "Plural friends takes the base verb meet."),
            q("Choose the routine with a negative.", ["She doesn't study on Sundays.", "She don't studies on Sundays.", "She doesn't studies on Sundays."], 0, "Doesn't is followed by the base verb study."),
            q("Our teacher ___ two languages.", ["speak", "speaking", "speaks"], 2, "Our teacher is singular, so use speaks."),
            q("They ___ work at weekends.", ["don't", "doesn't", "isn't"], 0, "Use don't with they in a present simple negative."),
        ]),
        "b2": ("Ask: is the action happening now? Use subject + am/is/are + -ing.\nI am waiting. You are waiting. He is waiting.\nFor a question, move am/is/are to the front: Are you waiting?", [
            q("Please be quiet. The baby ___ now.", ["sleeps every night", "is sleeping", "sleep"], 1, "Is sleeping describes an action in progress."),
            q("I ___ for the bus at the moment.", ["am waiting", "is waiting", "waits"], 0, "I takes am + waiting."),
            q("Which sentence is a correct negative?", ["They not are studying.", "They doesn't studying.", "They aren't studying."], 2, "Put not after are: are not / aren't."),
            q("___ you reading this message now?", ["Do", "Are", "Is"], 1, "Use Are you + verb-ing for an action happening now."),
        ]),
        "i1": ("Look for a finished time: yesterday, last week, in 2019 → past simple.\nNo finished time, experience up to now → have/has + past participle.\nSince tells you when a continuing situation began; for tells you its duration.", [
            q("She ___ her keys yesterday and found them this morning.", ["has lost", "lose", "lost"], 2, "Yesterday calls for the past simple lost."),
            q("I have known Jo ___ ten years.", ["for", "since", "ago"], 0, "For introduces a duration."),
            q("Have you ever ___ a marathon?", ["ran", "run", "running"], 1, "The past participle of run is run."),
            q("We ___ here in 2018. We still live here.", ["have moved", "moving", "moved"], 2, "In 2018 specifies a finished past time, even though we still live here."),
        ]),
        "i2": ("Decide whether the situation is a realistic future possibility or an imagined situation.\nReal: If I have time tomorrow, I will help.\nImagined: If I had more time, I would help.\nThe past form in the second example signals distance from reality, not past time.", [
            q("I don't know the answer. If I knew it, I ___ you.", ["will tell", "would tell", "tell"], 1, "An imagined present situation takes would + base verb."),
            q("If the shop is open tomorrow, we ___ some bread.", ["will buy", "would bought", "bought"], 0, "This is a real future possibility."),
            q("Which is an imagined present situation?", ["If it rains tomorrow, I'll stay in.", "If I see Jo, I'll say hello.", "If I were taller, I would play basketball."], 2, "Were taller signals an unreal present situation."),
            q("If you practise regularly, your fluency ___ improve.", ["would have", "will", "had"], 1, "A realistic future result can use will + base verb."),
        ]),
        "u1": ("Separate certainty from possibility.\nStrong yes about the past: must have left.\nPossible explanation: might have left.\nStrong no: can't have left.\nAlways follow have with a past participle, such as left, seen or forgotten.", [
            q("The parcel isn't here. It ___ been delivered to a neighbour; I'm not sure.", ["might have", "must", "can't"], 0, "Might have expresses a possible past explanation."),
            q("Choose the grammatically complete past deduction.", ["She must has left.", "She must have went.", "She must have gone."], 2, "Use modal + have + past participle gone."),
            q("I saw him at the office at noon. He ___ been at home at that exact time.", ["must have", "can't have", "might"], 1, "The evidence rules out his being at home then."),
            q("All the food is gone and the plates are dirty. They ___ eaten already. (strong deduction)", ["must have", "can't have", "must had"], 0, "Must have eaten is a strong positive deduction."),
        ]),
        "u2": ("Put a time label on each clause.\nPast cause: if + had + past participle.\nPresent result: would + base verb + now.\nIf I had taken that course (past), I would know the software now (present).", [
            q("If she had caught the earlier train, she ___ here now.", ["would have been yesterday", "would be", "will have"], 1, "Would be describes the present result."),
            q("If I ___ my keys, I wouldn't be locked out now.", ["would bring", "bring", "had brought"], 2, "Had brought is the unreal past cause."),
            q("What does 'If I had trained, I would be fitter now' imply?", ["I didn't train, and I'm not as fit now.", "I will train tomorrow.", "I trained and was fit last year."], 0, "The unreal past cause explains the unreal present result."),
            q("Choose a past-to-present mixed conditional.", ["If I study, I will pass.", "If I had slept well, I wouldn't feel tired now.", "If I had slept well, I would have felt better yesterday."], 1, "Had slept refers to the past; feel tired now refers to the present."),
        ]),
        "a1": ("Move a restrictive expression to the front for emphasis, then put the auxiliary before the subject.\nNever have I seen this. Only later did I notice it.\nIf you add did, change the main verb back to its base form: did I notice, not did I noticed.", [
            q("Never ___ such a difficult decision.", ["I had faced", "had I faced", "had faced I"], 1, "Fronted Never triggers auxiliary–subject inversion."),
            q("Only after reading the report ___ the error.", ["did he notice", "he noticed", "did he noticed"], 0, "Use did he notice in the main clause."),
            q("Not until the data were checked ___ the findings.", ["we published", "did published we", "did we publish"], 2, "The main clause is inverted: did we publish."),
            q("Rarely ___ so clearly.", ["she explains", "does she explain", "does she explains"], 1, "Use does + subject + base verb after Rarely."),
        ]),
        "a2": ("Ask what the evidence actually supports. A correlation supports an association, not a causal conclusion.\nChoose a clear hedge: may suggest; appears to.\nThen state the population or limitation: in this sample. Precision matters more than adding many uncertainty words.", [
            q("Which statement avoids an unsupported causal claim?", ["Coffee causes all anxiety.", "This survey proves coffee creates anxiety.", "Coffee intake was associated with reported anxiety in this sample."], 2, "An association in a sample does not establish a universal cause."),
            q("Which phrase marks appropriate uncertainty?", ["may suggest", "proves beyond doubt", "always guarantees"], 0, "May suggest calibrates the strength of a claim."),
            q("A result comes from one small pilot study. Which conclusion is best?", ["The result is true for everyone.", "The result warrants further investigation.", "No future study could change this conclusion."], 1, "A pilot result calls for investigation, not universal certainty."),
            q("Which sentence states scope most clearly?", ["Everyone behaves this way.", "The effect is certainly universal.", "Among the participants surveyed, most preferred option A."], 2, "Among the participants surveyed explicitly limits the scope."),
        ]),
    }
    for items in lessons.values():
        for item in items:
            remedial, extra = additions[item["id"]]
            item["remedial"] = remedial
            item["questions"].extend(extra)

    new = {
        "starter": [
            lesson("s3", "People: I, you, she, he", "🙂 I am Sam.\n👉 You are Alex.\n👩 She is Kim.\n👨 He is Jo.\n\nI → am. You → are. She/he → is.\nExample: Hello! I am Sam. You are Alex.", [
                q("I ___ Sam.", ["am", "is", "are"], 0, "Use I am."),
                q("You ___ Alex.", ["am", "are", "is"], 1, "Use you are."),
                q("She ___ Kim.", ["are", "am", "is"], 2, "Use she is."),
                q("He ___ Jo.", ["is", "are", "am"], 0, "Use he is."),
                q("Choose the correct sentence.", ["I is Sam.", "I am Sam.", "I are Sam."], 1, "I goes with am."),
                q("Choose the correct sentence about Alex.", ["You is Alex.", "You am Alex.", "You are Alex."], 2, "You goes with are."),
                q("Complete: ___ is Kim. 👩", ["She", "I", "You"], 0, "She goes with is."),
            ]),
            lesson("s4", "Simple requests", "💧 Water, please.\n🍎 An apple, please.\n🙏 Thank you.\n🙂 You're welcome.\n\nPlease makes a request polite. Say 'Thank you' when someone helps you. Reply 'You're welcome'.", [
                q("💧 Ask politely for water.", ["Water, please.", "Goodbye water.", "My name water."], 0, "Please makes the request polite."),
                q("Someone gives you water. Say:", ["Three.", "Thank you.", "My name."], 1, "Thank you expresses thanks."),
                q("Someone says 'Thank you'. Reply:", ["Apple, please.", "I am Sam.", "You're welcome."], 2, "You're welcome is a reply to thanks."),
                q("Complete: An apple, ___.", ["please", "name", "hello"], 0, "Please makes this request polite."),
                q("Which phrase expresses thanks?", ["Goodbye.", "Thank you.", "Water, please."], 1, "Thank you expresses thanks."),
                q("You want an apple. Choose the request.", ["You're welcome.", "Goodbye.", "An apple, please."], 2, "This politely asks for an apple."),
                q("Complete the reply: Thank you! — You're ___.", ["welcome", "please", "apple"], 0, "You're welcome is the complete reply."),
            ]),
        ],
        "beginner": [
            lesson("b3", "Past events", "Use the past simple for finished events. Regular verbs add -ed: visit → visited.\nSome verbs are irregular: go → went; see → saw.\nUse didn't + base verb for negatives: I didn't go.\nQuestions: Did you visit the museum?", [
                q("Yesterday we ___ the museum.", ["visited", "visit", "visiting"], 0, "Yesterday is finished past time; use visited."),
                q("Last week she ___ to Rome.", ["go", "went", "gone"], 1, "The past simple of go is went."),
                q("Choose the correct negative.", ["I didn't went.", "I don't went.", "I didn't go."], 2, "Use didn't + base verb go."),
                q("___ you visit the park yesterday?", ["Did", "Do", "Are"], 0, "Use Did for a past simple question."),
                q("I ___ Jo at the station last night.", ["see", "saw", "seen"], 1, "Saw is the past simple of see."),
                q("Which sentence describes a finished past event?", ["I visit Jo every day.", "I am visiting Jo.", "I visited Jo last Monday."], 2, "Last Monday is a finished time."),
                q("Did she ___ the film?", ["see", "saw", "seen"], 0, "After did, use the base verb see."),
            ]),
            lesson("b4", "Plans and travel arrangements", "Use be going to + base verb for an intention: I'm going to visit Jo.\nUse the present continuous for an arranged future event: I'm meeting Jo at six; we booked a table.\nUse will for a decision made now: The phone is ringing. I'll answer it.\nLook for context, not just a time word.", [
                q("I have decided on my holiday plan. I ___ visit Spain.", ["am going to", "going", "am go"], 0, "Be going to + base verb expresses an intention."),
                q("We booked a table. We ___ Jo there at six.", ["meeting", "are meeting", "met yesterday"], 1, "Present continuous can describe a future arrangement."),
                q("The phone is ringing. I ___ answer it!", ["answering", "answered", "will"], 2, "Will is natural for a decision made now."),
                q("She is going to ___ a train ticket.", ["buy", "bought", "buying"], 0, "Use the base verb after going to."),
                q("Choose the complete plan.", ["They going to travel.", "They are going to travel.", "They are go to travel."], 1, "Use are going to + travel."),
                q("Which sentence describes a booked arrangement?", ["I met Jo yesterday.", "I meet Jo every day.", "I'm meeting Jo tomorrow; our tickets are booked."], 2, "The booking supports a future arrangement."),
                q("Choose a spontaneous offer.", ["Those bags look heavy. I'll help you.", "I helped you yesterday.", "I help you every week."], 0, "I'll help makes an offer now."),
            ]),
        ],
        "intermediate": [
            lesson("i3", "Reading a problem and proposing a solution", "A problem–solution text explains what is wrong, why it matters, and a practical response.\nBecause introduces a reason. So introduces a result. However introduces a contrast.\nExample: Buses are crowded because demand is high. Adding morning services could reduce crowding. However, it would cost more.", [
                q("Buses are crowded because demand is high. What is the stated cause?", ["High demand", "Low ticket prices", "Empty roads"], 0, "The clause after because states the cause."),
                q("Which is a proposed solution to crowded buses?", ["Buses are crowded.", "Add more morning services.", "Demand is high."], 1, "Adding services responds to the problem."),
                q("Adding buses helps. ___, it costs more.", ["Because", "So", "However"], 2, "However introduces the contrast between benefit and cost."),
                q("The library closes early, ___ evening students cannot use it.", ["so", "because", "although"], 0, "So introduces the result of early closing."),
                q("Which proposal directly addresses an early library closing time?", ["Describe the library's colour.", "Extend opening hours on two evenings.", "Count chairs at home."], 1, "Longer opening hours address access in the evening."),
                q("The bus service is useful. However, it is expensive. What follows 'However'?", ["A repeated benefit", "An unrelated greeting", "A drawback"], 2, "The cost contrasts with the benefit."),
                q("Choose a sentence giving a reason.", ["The road is closed because repairs are underway.", "The road is closed. Goodbye.", "The road will open soon. Hello."], 0, "Because introduces why the road is closed."),
            ]),
            lesson("i4", "Reported messages", "When reporting a past message, we often move the tense back.\n'I am busy,' Jo said. → Jo said that she was busy.\n'We have finished,' they said. → They said that they had finished.\nChange pronouns to match the speaker.\nTell needs a person: Jo told me ... Say does not: Jo said ...", [
                q("Jo said, 'I am tired.' Choose a backshifted report.", ["Jo said she was tired.", "Jo said I am tired.", "Jo told she tired."], 0, "Am changes to was; I refers to Jo, so use she."),
                q("They said, 'We have finished.' Report it with backshift.", ["They said we finish.", "They said they had finished.", "They told had finish."], 1, "Have finished changes to had finished."),
                q("Choose the correct use of tell.", ["She told that she was busy.", "She told to busy.", "She told me that she was busy."], 2, "Tell normally needs the listener as an object."),
                q("Choose the correct sentence.", ["He said he was ready.", "He said me he was ready.", "He told he was ready."], 0, "Say does not take the listener directly as an object."),
                q("Sam said, 'I am ready.' With backshift: Sam said ___ ready.", ["I was", "he was", "he were"], 1, "The pronoun refers to Sam; am backshifts to was."),
                q("Which is a backshifted report of 'We are late'?", ["They said we is late.", "They said they late.", "They said they were late."], 2, "Are changes to were; we changes to they."),
                q("Complete: Jo ___ me that the train was delayed.", ["told", "said", "say"], 0, "Told takes me as its object."),
            ]),
        ],
        "upper": [
            lesson("u3", "Evaluating an argument", "Separate a claim, its evidence and its assumption.\nClaim: We should build a cycle lane. Evidence: Cycling trips have doubled.\nAssumption: A cycle lane would address cyclists' needs.\nA counterargument challenges the proposal. A concession acknowledges a valid opposing point without abandoning the argument.\nExample: Although space is limited, safer cycling may justify reallocating road space.", [
                q("'We should build a cycle lane.' This is the argument's:", ["Claim", "Numerical evidence", "Concession"], 0, "It states what the writer wants us to accept."),
                q("'Cycling trips have doubled.' This functions as:", ["A greeting", "Evidence", "A recommendation"], 1, "It supplies information supporting the proposal."),
                q("Which sentence concedes a drawback?", ["There are no drawbacks.", "The proposal is perfect.", "Although space is limited, the safety benefits matter."], 2, "Although acknowledges a real limitation."),
                q("Which question tests the proposal's assumption?", ["Would the planned lane meet cyclists' actual needs?", "How do you spell lane?", "What is the author's first name?"], 0, "This tests the link between the evidence and the proposed response."),
                q("Which is a counterargument to the lane proposal?", ["Cycling has grown.", "Removing a bus lane could delay more commuters.", "The lane is proposed."], 1, "It raises a reason against the proposal."),
                q("Which response engages constructively with a counterargument?", ["Anyone who disagrees is foolish.", "Ignore every cost.", "We should compare bus delays with the safety gains before deciding."], 2, "It evaluates the competing considerations."),
                q("Which is evidence rather than a recommendation?", ["The survey recorded 600 daily cyclists.", "Build the lane immediately.", "We ought to change the road."], 0, "The survey result is supporting information, not an instruction."),
            ]),
            lesson("u4", "Diplomatic disagreement", "In professional discussions, acknowledge the other view and explain your concern.\n'I see your point; however, the deadline may be unrealistic.'\nUse could/might to propose alternatives: 'Could we test a smaller version first?'\nAsk for clarification rather than assuming: 'When you say ready, do you mean tested or only drafted?'", [
                q("Which reply disagrees diplomatically?", ["I see your point, but the cost concerns me.", "That's stupid.", "You never think."], 0, "It acknowledges the view and states a specific concern."),
                q("Which proposes an alternative politely?", ["Do exactly what I say.", "Could we test a smaller version first?", "Your idea is worthless."], 1, "Could we introduces a collaborative proposal."),
                q("A colleague says the report is ready. Which asks for clarification?", ["You're wrong.", "That means nothing.", "Do you mean drafted or fully reviewed?"], 2, "The question clarifies the meaning of ready."),
                q("Which focuses on the issue rather than attacking a person?", ["The deadline leaves no time for testing.", "You're incompetent.", "Only you would suggest this."], 0, "It identifies a practical problem with the timeline."),
                q("Complete a tentative suggestion: We ___ extend the trial by a week.", ["musted", "might", "are"], 1, "Might makes the suggestion tentative."),
                q("Which response both acknowledges and qualifies?", ["No, never.", "Obviously you're wrong.", "The idea has merit, though we need a clearer budget."], 2, "It recognises value while specifying a concern."),
                q("Which question invites a practical compromise?", ["Could we agree on a smaller first release?", "Why are you always wrong?", "Who cares about testing?"], 0, "It proposes a concrete shared next step."),
            ]),
        ],
        "advanced": [
            lesson("a3", "Implication and pragmatic meaning", "Meaning can be implied rather than stated. Interpret the words in context and avoid claiming more certainty than the context supports.\nAfter a poor performance, 'Well, that went brilliantly' may be ironic.\n'The room is rather warm' may indirectly request an open window.\nIn a reference, 'She is always punctual' may imply faint praise if relevant expertise is conspicuously omitted. Such readings depend on context.", [
                q("After an obvious failure, someone says 'That went brilliantly.' The likely reading is:", ["Irony", "A literal success report", "A request for directions"], 0, "The words conflict with the shared context, suggesting irony."),
                q("A guest near a closed window says 'It's rather warm in here.' This may function as:", ["A formal resignation", "An indirect request to open the window", "Proof the heater is broken"], 1, "The remark can indirectly invite action; context matters."),
                q("Which interpretation is most careful?", ["Warm always means open the window.", "Every compliment is ironic.", "The remark may be a request, depending on the context."], 2, "Pragmatic interpretations depend on context."),
                q("A reference mentions only punctuality for a highly technical role. A reader might infer:", ["Limited praise for technical competence", "Proof of excellent technical skills", "A guaranteed promotion"], 0, "The omission may suggest faint praise, but does not prove incompetence."),
                q("What best distinguishes an implication from an explicit statement?", ["An implication is always false.", "An implication is inferred using context.", "An implication has no meaning."], 1, "Listeners infer implications beyond the literal wording."),
                q("What evidence most helps identify irony?", ["The number of letters alone", "Whether the word is long", "A mismatch between literal praise and the known outcome"], 2, "Context can make a literal interpretation implausible."),
                q("Which conclusion avoids overinterpretation of faint praise?", ["The omission may be meaningful, but more context is needed.", "The employee is certainly unqualified.", "Every short reference is negative."], 0, "A possible implication is not conclusive evidence."),
            ]),
            lesson("a4", "Synthesising sources", "Synthesis organises sources around a shared issue rather than listing them one by one.\nExample: Study A finds a benefit in adults; Study B finds no effect in children.\nA precise synthesis identifies agreement, contrast and scope: 'The effect may depend on age; the two studies examine different populations.'\nAttribute claims, distinguish evidence from inference, and do not invent agreement.", [
                q("A finds a benefit in adults; B finds none in children. Which synthesis is most precise?", ["The difference may relate to the populations studied.", "Both prove a universal benefit.", "B proves A is fraudulent."], 0, "Different populations may explain contrasting results."),
                q("What distinguishes synthesis from a source-by-source list?", ["Removing all source attribution", "Organising evidence around a shared question", "Quoting every sentence"], 1, "Synthesis relates evidence across sources."),
                q("Which phrase clearly attributes a finding?", ["Everyone knows ...", "It is beyond all doubt ...", "Study A reports a benefit among adults."], 2, "The source and population are explicit."),
                q("Which is an inference rather than a reported result?", ["The difference may reflect age-related factors.", "Study A recorded 60 participants.", "Study B reported no measurable effect."], 0, "May reflect introduces an explanatory interpretation."),
                q("Two studies examine different age groups. What should a synthesis preserve?", ["Only the more exciting result", "The difference in population and scope", "An invented consensus"], 1, "Scope matters when comparing results."),
                q("Which conclusion would require more evidence?", ["A studied adults.", "B studied children.", "Age definitely caused the difference in findings."], 2, "Population differences alone do not prove the causal explanation."),
                q("Which sentence combines contrast and attribution?", ["While A reports adult benefits, B finds no effect in children.", "All research agrees on everything.", "One source exists, and another source exists."], 0, "It relates the attributed findings through a clear contrast."),
            ]),
        ],
    }
    for level, items in new.items():
        for item in items:
            # The alternative is a worked example and guided reasoning, not the original text.
            item["remedial"] = REMEDIAL[item["id"]]
        lessons[level].extend(items)


REMEDIAL = {
    "s3": "Read each pair: I → am; you → are; she → is; he → is.\nNow add a name: I am Sam. She is Kim.\nTry: He ___ Jo. Answer: is.",
    "s4": "💧 You want water: Water, please.\n🤝 You get water: Thank you.\n🙂 Someone thanks you: You're welcome.\nMatch each phrase to the moment: ask → please; receive → thank you; reply → you're welcome.",
    "b3": "Find a finished time first: yesterday / last week.\nPositive: We visited. I went.\nNegative: didn't already marks the past; use didn't go.\nQuestion: Did + subject + base verb: Did she see it?",
    "b4": "Choose from the situation.\nA decision made before speaking: I'm going to travel.\nAn agreed booking: I'm meeting Jo tomorrow.\nA decision made now: I'll help!\nDon't omit am/is/are in going to or present continuous forms.",
    "i3": "Work through a short example: The room is noisy because traffic is heavy. We could close the window. However, the room might get hot.\nProblem: noise. Cause: traffic. Solution: close window. Drawback: heat.\nFind what each sentence does before choosing a linker.",
    "i4": "Start with Jo's words: 'I am ready.'\nWho is I? Jo → she.\nBackshift am → was.\nResult: Jo said she was ready.\nIf you name the listener, use told me, not said me.",
    "u3": "Take the claim 'Extend the library hours.' A usage survey is evidence. The idea assumes people will attend later. Staffing costs are a counterargument.\nA concession can admit the cost while explaining why access is worth it. Label each part before evaluating the argument.",
    "u4": "Rewrite an attack as a specific concern.\n'Your plan is terrible' → 'The plan leaves little testing time.'\nThen acknowledge a benefit and offer an alternative: 'The scope is useful. Could we release it in two stages?'",
    "a3": "Use three steps: literal wording → shared context → plausible intention.\n'Wonderful!' after a failed test conflicts with the outcome, so irony is plausible.\nWithout that context, praise may be sincere. Treat interpretations as inferences, not guaranteed facts.",
    "a4": "Create two columns: what each source reports, and your interpretation.\nA: adult benefit. B: no child benefit.\nInterpretation: age may matter.\nA synthesis connects these points while keeping the age explanation tentative and attributing each result.",
}

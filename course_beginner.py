"""Original A1/A2 units covering grammar and everyday communication."""
from course_authoring import unit

UNITS = [
unit("b05", "Articles: a, an, the and no article", "A2", "grammar", "Introduce something and refer back to it.",
"Use a/an for one non-specific countable item: I bought a pen. Use the when the listener can identify it: The pen is blue. Use no article for plural or uncountable nouns in a general statement: Cats sleep. Water is essential. Choose a/an by sound: a university, an hour.",
"First mention: a bag. Second mention: the bag. General plural: bags. Listen to the next sound: university starts with a /y/ sound; hour starts with a vowel sound.",
"""I saw ___ dog. The dog was small. | a | the only | an | 0 | A introduces one non-specific dog.
I bought a book. ___ book is red. | A | The | An | 1 | The refers back to the identified book.
___ water is essential for life. (general statement) | A | An | No article | 2 | General uncountable water has no article.
Choose by pronunciation. | an hour | a hour | an university | 0 | The h in hour is silent.
Choose the general statement. | The cats are always the animals. | Cats are animals. | A cats are animals. | 1 | General plural nouns normally take no article.
She studies at ___ university. | an | no article | a | 2 | University begins with a consonant /y/ sound.
Close the door means the speaker expects: | you can identify the door | any door anywhere | that no door exists | 0 | The signals an identifiable referent.""",
"Describe a room: introduce three items, then refer to each again using the."),
unit("b06", "Countable nouns and quantities", "A2", "grammar", "Ask and answer about quantities of countable and uncountable things.",
"Countable nouns have singular and plural forms: an apple, three apples. Uncountable nouns such as water and information are not normally counted directly. Use many with plural countable nouns and much with uncountable nouns. Use some in many positive statements and any in many questions and negatives. A bottle of water counts the container.",
"Ask: can I count the noun directly? Apples → how many. Water → how much. To count water, add a unit: two bottles of water. Use a piece of information, not an information.",
"""How ___ apples do we need? | many | much | an | 0 | Apples is plural and countable.
How ___ water is left? | many | much | a | 1 | Water is uncountable.
Choose the standard phrase. | two informations | an information | a piece of information | 2 | Information is normally uncountable.
We haven't got ___ milk. | any | many | a | 0 | Any is natural in this negative.
Choose a countable noun. | water | apple | advice | 1 | One apple, two apples.
We need two ___ of water. | waters bottle | water | bottles | 2 | Count the containers: two bottles.
Which asks about an uncountable quantity? | How much rice? | How many rice? | How a rice? | 0 | Rice is normally uncountable.""",
"Make a shopping list using three countable items and three uncountable items with suitable quantities."),
unit("b07", "Comparatives and superlatives", "A2", "grammar", "Compare two things and identify an extreme within a group.",
"A comparative compares: small → smaller; expensive → more expensive. Use than: This bag is cheaper than that one. A superlative identifies an extreme in a group: the smallest, the most expensive. Irregular forms include good/better/best and bad/worse/worst. Do not combine more with an -er comparative.",
"Two alternatives: cheaper than. A whole group: the cheapest. Long adjective: more useful, the most useful. Good is irregular: better, best.",
"""This bag is ___ than that one. | cheaper | cheapest | more cheaper | 0 | Use one comparative form, cheaper.
This is ___ expensive option in the shop. | more | the most | most than | 1 | A group extreme uses the most.
Good → comparative: | gooder | best | better | 2 | Better is irregular.
Choose the correct comparison. | taller than | tallest than | more taller | 0 | Comparative taller takes than.
Among all five routes, this is ___. | shorter than | the shortest | most shorter | 1 | The shortest identifies the group extreme.
Bad → superlative: | baddest | worse | worst | 2 | Worst is the irregular superlative.
Choose the correct phrase. | more useful | usefuller most | more usefuler | 0 | Use more with useful.""",
"Compare three places you know using two comparatives and two superlatives."),
unit("b08", "Rules, obligations and advice", "A2", "function", "Distinguish a prohibition from advice and a lack of obligation.",
"Must and have to can express obligation: You must wear a helmet. You have to show a ticket. Mustn't means something is prohibited. Don't have to means it is optional. Should gives advice: You should rest. Follow modals with the base verb. Context decides how strong the message is.",
"Ask whether the action is required, forbidden or optional. Must: required. Mustn't: forbidden. Don't have to: optional. Should: recommended, usually less strong than a rule.",
"""Entry is forbidden. You ___ enter. | mustn't | don't have to | should | 0 | Mustn't expresses prohibition.
Attendance is optional. You ___ attend. | mustn't | don't have to | must | 1 | Don't have to means there is no obligation.
Which gives advice? | You must show a passport. | You mustn't park here. | You should get some rest. | 2 | Should introduces advice.
You must ___ a ticket. | buy | buys | buying | 0 | Use a base verb after must.
Which means required? | You may skip it. | You have to do it. | You don't have to do it. | 1 | Have to expresses obligation here.
Don't have to means: | forbidden | impossible | optional | 2 | Lack of obligation is not prohibition.
Choose the advice form. | You should drink some water. | You should drinks water. | You should drinking water. | 0 | Should takes the base verb.""",
"Write two rules, one optional action and two pieces of advice for a fictional club."),
unit("b09", "Requests, permission and offers", "A2", "interaction", "Make a polite request and ask permission.",
"Can you ...? asks someone to act. Could you ...? is often more polite: Could you open the window? Can I ...? asks permission: Can I sit here? Would you like ...? makes an offer: Would you like some tea? Match the phrase to who will perform the action.",
"Identify the actor. Could you carry this? → the listener acts. Can I use this? → the speaker asks permission to act. Would you like tea? → the speaker offers tea.",
"""Ask someone politely to open a window. | Could you open the window? | Can I open the window? | Would you like a window? | 0 | Could you requests the listener's action.
Ask permission to sit. | Could you sit? | Can I sit here? | You must sit. | 1 | Can I asks permission for the speaker.
Offer a drink. | You drink now. | Can I drink? | Would you like some tea? | 2 | Would you like introduces an offer.
Could you help me? — a suitable acceptance: | Of course. | I am a chair. | Yesterday only. | 0 | Of course agrees to help.
Which phrase is generally more polite for a request? | Open it! | Could you open it, please? | Open! Now! | 1 | Could you and please soften the request.
Who acts in 'Could you carry this?' | Nobody | The speaker only | The listener | 2 | You refers to the listener.
Decline an offer politely. | No, thank you. | Never speak. | You are wrong. | 0 | No, thank you is a polite refusal.""",
"Write a cafe dialogue including a request, permission question, offer and polite refusal."),
unit("b10", "Past continuous and interrupted actions", "A2", "grammar", "Describe an action in progress at a past time.",
"Use was/were + -ing for an action in progress in the past. At eight, I was cooking. They were studying. The past simple can describe an event during that action: I was cooking when the phone rang. While often introduces the longer background action. Was goes with I/he/she/it; were with you/we/they.",
"Draw a long line for was cooking, and a point for rang. The line gives background; the point is the event. Use was/were with the subject, then add -ing.",
"""At nine last night, I ___ studying. | was | were | am | 0 | I takes was in this past form.
They ___ waiting when I arrived. | was | were | is | 1 | They takes were.
I was cooking when the phone ___. | ringing | was ring | rang | 2 | Rang is the past simple event.
Choose the background action. | She was reading. | The glass broke. | The door slammed. | 0 | Was reading describes an action in progress.
While we ___, it started to rain. | walk | were walking | was walking | 1 | We takes were walking for background.
Choose the correct form. | He were sleeping. | He was sleep. | He was sleeping. | 2 | Use was + -ing with he.
What was happening at the time of the call? 'I was driving when Jo called.' | Driving | Calling Jo repeatedly | Finishing a journey, explicitly | 0 | Driving was in progress; the sentence does not specify a completed journey.""",
"Write a five-sentence story with two background actions and two interrupting events."),
unit("b11", "Infinitives and -ing after common verbs", "A2", "grammar", "Use basic verb patterns after want, decide and enjoy.",
"Some verbs are followed by to + base verb: want to learn, decide to leave. Others are followed by -ing: enjoy reading, finish cooking. A preposition is usually followed by a noun or -ing form: interested in learning. The pattern belongs to the verb or phrase; learn the whole expression.",
"Group useful chunks: want to go; decide to go; enjoy going; finish going. After in, use learning rather than to learn. Do not assume all verbs share one pattern.",
"""I want ___ English. | to learn | learning only | learn to | 0 | Want normally takes a to-infinitive.
She enjoys ___. | to swim | swimming | swim to | 1 | Enjoy takes an -ing complement.
We decided ___ early. | leaving | leave | to leave | 2 | Decide takes a to-infinitive.
He finished ___ dinner. | cooking | to cook | cook to | 0 | Finish takes an -ing form.
I am interested in ___ abroad. | to study | studying | study to | 1 | A preposition such as in is followed by -ing.
Choose the correct chunk. | enjoy to read | want reading always | want to read | 2 | Want to read is the standard pattern.
Which belongs with enjoy? | reading | to reading | read to | 0 | Enjoy takes reading.""",
"Write about three things you want to do and three activities you enjoy doing."),
unit("b12", "Frequency and adverb position", "A2", "grammar", "Say how often an activity happens.",
"Frequency words range from always to usually, often, sometimes, rarely and never. They usually come before a main verb: I often walk. They come after be: She is often busy. Never already has negative meaning: I never smoke, not I don't never smoke in standard English. Every day means each day; everyday is an adjective.",
"Find the verb type. With work, put often first: often work. With is, put often after: is often busy. Use only one standard negative with never.",
"""Choose the usual order. | I often walk. | I walk often always. | Often I am walk. | 0 | Frequency adverbs commonly precede a main verb.
Choose the usual order with be. | She often is busy always. | She is often busy. | She busy often is. | 1 | Often normally follows is.
Which means zero occasions? | usually | sometimes | never | 2 | Never means not at any time.
Choose standard English. | I never smoke. | I don't never smoke. | I never doesn't smoke. | 0 | Never already makes the meaning negative.
I practise ___: Monday, Tuesday and every other day. | everyday | every day | every days | 1 | Every day means each day.
Which is closest to most occasions? | never | rarely | usually | 2 | Usually indicates a high frequency.
Choose the adjective phrase. | everyday activities | every day activities always | every days activity | 0 | Everyday is an adjective meaning ordinary or routine.""",
"Describe your weekly routine using always, usually, sometimes and never."),
unit("b13", "Subject, object and possessive forms", "A2", "grammar", "Choose a pronoun according to its role.",
"Subjects do the action: I, she, they. Objects receive it: me, her, them. She called me. Possessive determiners come before nouns: my bag, their books. Possessive pronouns stand alone: The bag is mine. These books are theirs. Its means belonging to it; it's means it is or it has.",
"Locate the slot. Before called → she. After called → me. Before bag → my. Without a following noun → mine. Expand it's to it is to test the apostrophe.",
"""___ called me. (Jo is female.) | She | Her | Hers | 0 | The subject form is she.
I called ___. (referring to several people) | they | them | their | 1 | The object form is them.
This bag belongs to me. It is ___. | my | me | mine | 2 | Mine stands without a following noun.
Choose the determiner phrase. | their books | theirs books | them books | 0 | Their precedes a noun.
___ raining. | Its | It's | It | 1 | It's means it is here.
The dog is wagging ___ tail. | it's | it is | its | 2 | Its is possessive.
These seats belong to us. They are ___. | ours | our | us | 0 | Ours is a possessive pronoun.""",
"Write a short lost-property exchange using she, her, my, mine, their and theirs."),
unit("b14", "Prepositions of time and movement", "A2", "grammar", "Use common time expressions and describe a route.",
"Use at for a time, on for a day/date and in for a month/year: at six, on Friday, in May, in 2025. We normally say next week without a preposition. Movement: to a destination, into an interior, out of an interior, across from one side to the other. Go home normally has no to.",
"Use a time ladder: clock → at; day → on; month/year → in. For movement, draw arrows: into a box, out of a box, across a road. Treat go home as a fixed pattern.",
"""Meet me ___ six. | at | on | in | 0 | Clock times normally take at.
The course starts ___ Monday. | at | on | in | 1 | Days normally take on.
We moved here ___ 2025. | on | at | in | 2 | Years normally take in.
Choose the usual phrase. | next week | in next week | on next week | 0 | Next week normally takes no preposition.
She walked from outside to inside the room: she walked ___ it. | out of | into | across above | 1 | Into marks movement to an interior.
Choose the usual phrase. | go to home | go at home | go home | 2 | Home used as a destination normally takes no to.
Cross from one side of the road to the other: walk ___ the road. | across | into | inside | 0 | Across marks movement from side to side.""",
"Give a route from your home to a fictional shop and include its opening day and time."),
unit("b15", "Shopping and service problems", "A2", "interaction", "Ask a price and describe a simple purchase problem.",
"Ask How much is this? for a price. In a shop, size and fit are different: size is the label; fit describes how it feels. This is too small means a larger size is needed. Keep a receipt as proof of purchase. A refund returns money; an exchange replaces the item. Use a clear polite request: Could I exchange this for a larger size?",
"State the problem before the request: These shoes are too small. Could I exchange them? Refund = money back. Exchange = another item. A receipt helps identify the purchase.",
"""Ask a price. | How much is this? | How old is this price? | Where much this? | 0 | How much asks for a price here.
The shoes are too small. You need: | a smaller size | a larger size | a lower age | 1 | Too small means a larger size is needed.
A refund gives you: | a different colour only | a receipt only | your money back | 2 | A refund returns the payment.
An exchange means: | replacing the purchased item | always receiving cash | changing your name | 0 | An exchange substitutes another item.
Which proves a purchase? | a weather report | a receipt | a timetable | 1 | A receipt records a purchase.
Choose a polite request. | Larger now! | You wrong! | Could I exchange this, please? | 2 | The form makes a clear polite request.
'This jacket fits well' describes: | how appropriately its shape and size suit the wearer | only its price | only its colour | 0 | Fit concerns how clothing suits the body.""",
"Write a six-line shop dialogue with a price question, problem, receipt and request for an exchange."),
unit("b16", "Notices and short messages", "A2", "reading", "Extract a condition, time or required action from a short notice.",
"Read for purpose first: is the message informing, requesting or warning? Then find details. 'Library closes at 6. Return books before closing' gives a time and an action. 'Staff only' limits access. 'Please reply by Friday' sets a deadline. By Friday means no later than Friday, not only on Friday.",
"Underline the action, then circle the time. Reply → action; by Friday → latest time. Staff only means the public cannot enter, not that staff must stay all day.",
"""'Please reply by Friday.' What must you do? | Send a response no later than Friday. | Reply only on Saturday. | Never reply. | 0 | By sets the latest time.
'Staff only' means access is for: | every visitor | employees | children only | 1 | Staff means employees.
'Library closes at 6.' The library is not open after: | 5 | 4 | 6 | 2 | Six is the stated closing time.
'Bring your ticket.' This is: | an instruction | an age question | a colour description | 0 | Bring requests an action.
'Meeting moved to Room 4.' What changed? | the date explicitly | the location | the organiser explicitly | 1 | Room 4 specifies the new location.
'Closed for repairs' gives: | a price | a person's name | a reason for closure | 2 | Repairs explain why it is closed.
'Return books before closing.' What is required? | Return them earlier than the closing time. | Return them after midnight. | Keep them forever. | 0 | Before means earlier than.""",
"Write an invitation with a place, time and reply deadline. Then write a polite acceptance."),
]

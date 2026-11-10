"""Original Pre-A1/A1 micro-lessons, with explicit visual and pronunciation limits."""
from course_authoring import unit

UNITS = [
unit("s05", "Letters, names and spelling", "Pre-A1", "literacy", "Recognise letters and spell a short name.",
     "English has 26 letters. Capital and small letters can name the same letter: A/a, B/b, C/c. Names start with a capital: Sam. When spelling a name, say each letter: Sam → S, A, M. A letter's name is not always its sound in a word. Learn names and sounds separately; text alone cannot teach their pronunciation.",
     "Match first: S and s are the same letter. Next split Sam into S + a + m. Keep the first letter capital when writing the name. Do not add or remove letters when spelling.",
     """Which pair is the same letter? | A / a | A / b | C / d | 0 | A and a are capital and small forms.
Which name starts with a capital? | sam | Sam | sAm | 1 | Names begin with a capital letter.
How is Kim spelled? | K, N, M | K, I | K, I, M | 2 | Kim has the letters K, I and M.
How many letters are in Jo? | Two | Three | One | 0 | Jo contains J and o.
Which letter comes after A in the alphabet? | D | B | Z | 1 | The alphabet starts A, B, C.
Choose the spelling of Alex. | A, L, E | A, E, L, X | A, L, E, X | 2 | Keep all letters in the correct order.
Which statement is correct? | A letter can have different sounds in different words. | Every letter has only one sound. | Capitals are different words. | 0 | Letter names and sounds are not identical concepts.""",
     "Write your first name, then write its letters separated by commas."),
unit("s06", "Vowels and first sounds", "Pre-A1", "pronunciation", "Notice vowel letters and distinguish spelling from sound.",
     "A, E, I, O and U are the main vowel letters; Y can also represent a vowel sound. A word needs sounds, not only letter names. Cat and cake both contain a, but the vowel sounds differ. Ship and sheep differ in their vowel sound and length/quality. These written examples are noticing exercises: ask a speaker or use trusted audio to hear and imitate the contrast.",
     "Circle the vowel letter in cat: a. Now compare cat and cake: the spelling changes the usual pronunciation. Do not pronounce a whole word by saying its alphabet letters. For ship/sheep, hear both words before trying the contrast.",
     """Which is a main vowel letter? | A | B | T | 0 | A is one of A, E, I, O, U.
Which word contains the vowel letter e? | cat | bed | cup | 1 | Bed is spelled b-e-d.
Which pair illustrates different vowel sounds? | cat / cat | bed / bed | ship / sheep | 2 | These words differ in vowel quality and usually duration.
Which is the vowel letter in cup? | u | c | p | 0 | Cup is spelled c-u-p.
Can you fully learn pronunciation from these written examples alone? | Yes, always | No, listening and speaking practice are also needed | Audio never helps | 1 | Pronunciation requires sound input and production.
Which pair both contains a but usually has different vowel sounds? | cat / cat | cake / cake | cat / cake | 2 | The letter a is pronounced differently in these examples.
Which letter can also represent a vowel sound? | Y | Only B | Only T | 0 | Y can represent a vowel, as in my.""",
     "Write cat, cake, ship and sheep. Ask a speaker to read them in random order and point to the word you hear; check together."),
unit("s07", "Numbers and age", "Pre-A1", "numeracy", "Recognise common numbers and give an age.",
     "4 four; 5 five; 6 six; 7 seven; 8 eight; 9 nine; 10 ten. 11 eleven; 12 twelve; 13 thirteen; 20 twenty; 30 thirty; 100 one hundred. Say your age with be: I am twenty. Ask: How old are you? Thirteen and thirty are different numbers; practise hearing their stress with audio.",
     "Use digits first: 13 → thirteen; 30 → thirty. For age, start I am, then add the number: I am thirty. Do not translate age as I have thirty.",
     """5 = ___ | five | four | nine | 0 | Five represents 5.
20 = ___ | twelve | twenty | thirteen | 1 | Twenty represents 20.
Choose the age sentence. | I have twenty. | I twenty years. | I am twenty. | 2 | Use be to state age.
How do you ask about age? | How old are you? | What colour are you? | Where is twenty? | 0 | How old asks for age.
13 = ___ | thirty | thirteen | three hundred | 1 | Thirteen is 13, not 30.
100 = ___ | ten | one thousand | one hundred | 2 | One hundred represents 100.
30 = ___ | thirty | thirteen | three | 0 | Thirty represents 30.""",
     "Write three fictional people's names and ages. Use a different number for each person."),
unit("s08", "A, an and everyday objects", "A1", "grammar", "Name a single object with a or an.",
     "Use a/an with one countable thing: a book, an apple. Choose by the next sound: a + consonant sound, an + vowel sound. An orange is one orange. This is a book names something near you. This is an apple. Do not use a/an directly before a plural noun.",
     "Count first: one object. Listen to its first sound: book starts with /b/, so a book. Apple starts with a vowel, so an apple. For two objects, use two books, not a books.",
     """This is ___ book. | a | an | two | 0 | Book begins with a consonant sound.
This is ___ apple. | a | an | three | 1 | Apple begins with a vowel sound.
Choose the correct phrase. | an books | a apples | an orange | 2 | Orange is singular and begins with a vowel sound.
Which phrase names one thing? | a pen | two pens | three books | 0 | A pen refers to one pen.
Complete: This ___ a bag. | are | is | am | 1 | This takes is.
Choose the plural phrase. | a books | an books | two books | 2 | Use a plural noun after two.
Choose the correct phrase. | a chair | an chair | a chairs | 0 | Chair begins with a consonant sound and is singular.""",
     "Name five objects around you with This is a/an ... ."),
unit("s09", "Plurals and these/those", "A1", "grammar", "Distinguish one object from several and near from far.",
     "Most nouns add -s: book/books. Some add -es: box/boxes. Some change form: child/children. Near: this book, these books. Far: that book, those books. Use is for this/that and are for these/those. These are books. Those are boxes.",
     "Ask two questions: one or more? Near or far? One near → this is. More than one near → these are. One far → that is. More than one far → those are.",
     """Two ___ | books | book | a book | 0 | Two requires plural books.
Several boxes are near you: ___ are boxes. | This | These | That | 1 | These refers to plural things nearby.
One bag is far away: ___ is a bag. | These | Those | That | 2 | That refers to one thing farther away.
Choose the plural of child. | children | childs | childes | 0 | Children is an irregular plural.
Complete: Those ___ pens. | is | are | am | 1 | Those takes are.
Choose the plural of box. | boxs | box | boxes | 2 | Box adds -es.
Which phrase refers to several things far away? | those chairs | this chair | that chair | 0 | Those is plural and usually distant.""",
     "Describe two nearby objects and two distant objects using this, these, that and those."),
unit("s10", "Colours and describing things", "A1", "vocabulary", "Use basic adjectives to describe an object.",
     "🔴 red; 🔵 blue; 🟢 green; 🟡 yellow. Other descriptions: big/small, old/new. An adjective can come before a noun: a small bag, a blue pen. It can follow be: The bag is small. English adjectives do not add a plural -s: two blue pens.",
     "Keep the adjective unchanged. One red bag → two red bags. Put the describing word before the noun, or use noun + is/are + adjective: The pens are blue.",
     """🔴 Which colour? | red | blue | green | 0 | The symbol is red.
Choose the normal word order. | a bag small | a small bag | small a bag | 1 | The adjective normally precedes the noun.
Choose the correct plural description. | blues pens | blue pen two | two blue pens | 2 | Blue stays unchanged; pens becomes plural.
Opposite of big: | small | red | new | 0 | Big and small describe contrasting sizes.
Complete: The bags ___ new. | is | are | am | 1 | Plural bags takes are.
🔵 Choose the phrase. | a green circle | a red circle | a blue circle | 2 | The symbol is blue.
Opposite of old, for a recently made object: | new | small | yellow | 0 | Old and new contrast in age.""",
     "Describe three real objects with a colour and one other adjective."),
unit("s11", "Family and possession", "A1", "grammar", "Introduce family members and say who something belongs to.",
     "Family words include mother, father, sister and brother. My identifies something connected to me; your identifies something connected to you. This is my sister. Her name is Kim. His name is Sam. Add 's to a person's name for possession: Kim's bag = the bag belonging to Kim.",
     "Separate the person from possession. She is Kim. Her bag is blue. He is Sam. His bag is red. For a name, use Kim's bag. My does not change to match the number of objects: my book, my books.",
     """This is ___ mother. (belonging to my family) | my | I | me | 0 | My comes before a noun.
Kim is my sister. ___ name is Kim. | His | Her | She | 1 | Her is the possessive form for she.
Sam is my brother. ___ name is Sam. | He | Him | His | 2 | His comes before name.
Kim's bag means: | the bag belonging to Kim | a bag named Friday | two bags | 0 | Apostrophe-s marks possession here.
Choose the correct phrase. | I sister | my sister | me sister | 1 | Use my before sister.
Which is a family word? | chair | yellow | brother | 2 | Brother names a family relationship.
Complete: These are ___ books. (belonging to me) | my | I | me | 0 | My is used with singular and plural nouns.""",
     "Introduce two fictional family members and describe one possession of each."),
unit("s12", "Days and clock time", "A1", "time", "Recognise days and give simple clock times.",
     "Days: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday. Use on with a day: on Monday. Use at with a clock time: at two o'clock. 2:00 = two o'clock; 2:30 = half past two. Ask: What time is it? Capitalise the names of days.",
     "Read the clock in two parts. 3:00 → three o'clock. 3:30 → half past three. Put at before the time, on before the day: at three on Monday.",
     """2:00 is: | two o'clock | half past two | three o'clock | 0 | :00 is o'clock.
2:30 is: | half past three | half past two | two o'clock | 1 | :30 is half past the hour.
Meet me ___ Monday. | at | in | on | 2 | Use on with a day.
The lesson starts ___ ten o'clock. | at | on | of | 0 | Use at with clock times.
Which asks for the time? | How old are you? | What time is it? | What colour is it? | 1 | What time asks about time.
The day after Monday is: | Sunday | Friday | Tuesday | 2 | Tuesday follows Monday.
Choose the correct spelling style. | on Friday | on friday | at friday | 0 | Days are capitalised and take on.""",
     "Write a three-day timetable with one activity and clock time on each day."),
unit("s13", "Where is it?", "A1", "space", "Describe a simple location.",
     "In means inside: the key is in the bag. On means on a surface: the book is on the table. Under means below: the cat is under the chair. Next to means beside. Ask: Where is the key? Answer: It is in the bag. The meaning comes from the spatial relationship, not from the object alone.",
     "Imagine a box. Inside the box → in. Resting on its top → on. Below it → under. Beside it → next to. Draw the scene before choosing a word.",
     """The key is inside the bag. It is ___ the bag. | in | on | under | 0 | In describes an inside position.
The book rests on the table's top surface. It is ___ the table. | in | on | under | 1 | On describes contact with the upper surface here.
The cat is below the chair. It is ___ it. | on | in | under | 2 | Under means below.
Which question asks for location? | Where is the bag? | How old is the bag? | What colour is the bag? | 0 | Where asks about place.
Beside the chair means: | inside it | next to it | above it | 1 | Next to means beside.
Complete: Where ___ the key? | are | am | is | 2 | Singular key takes is.
Two pens are inside a box. Choose the sentence. | The pens are in the box. | The pens is on the box. | The pens am under the box. | 0 | Plural pens takes are; inside means in.""",
     "Draw a room and write four sentences locating objects in, on, under or next to something."),
unit("s14", "There is and there are", "A1", "grammar", "Say what exists in a place.",
     "Use there is with one thing: There is a chair. Use there are with more than one: There are two chairs. A negative says something is absent: There isn't a table. Questions change the order: Is there a chair? Are there two chairs? These sentences introduce what is in a place.",
     "Count the noun, then select the form. A chair → there is. Two chairs → there are. For a question, move is/are first: Is there ...? Are there ...?",
     """There ___ a chair. | is | are | am | 0 | A chair is singular.
There ___ two windows. | is | are | am | 1 | Two windows is plural.
Choose a question. | There a chair is? | A chair there? | Is there a chair? | 2 | Put is before there in the question.
The room has no table. | There isn't a table. | There is a table. | There are a table. | 0 | Isn't makes the singular negative.
___ there three books? | Is | Are | Am | 1 | Three books requires are.
Choose the correct sentence. | There is two bags. | There am a bag. | There are two bags. | 2 | Use there are for plural things.
What does 'There is a lamp' tell us? | A lamp exists in the place. | The lamp's age | The lamp's price | 0 | There is introduces the presence of something.""",
     "Describe what is and is not in a room using there is, there are and there isn't."),
unit("s15", "Can: simple abilities", "A1", "function", "Say what you can and cannot do.",
     "Can + base verb describes ability: I can swim. She can read. Can does not add -s with she/he. Cannot or can't is negative: I can't swim. Questions put can first: Can you swim? Short answers: Yes, I can. No, I can't.",
     "Keep the action unchanged after can. He can swim, not he can swims. To ask, use Can + person + action? To deny the ability, use can't + action.",
     """She can ___ English. | read | reads | reading | 0 | Use the base verb after can.
I cannot swim means: | I swim every day. | I am not able to swim. | I love swimming. | 1 | Cannot expresses lack of ability here.
Choose the question. | You can swim? only | Swim you can? | Can you swim? | 2 | Can comes before the subject in the standard question.
Choose the correct sentence. | He can cook. | He cans cook. | He can cooks. | 0 | Can and the base verb stay unchanged.
Can you read? — Yes, I ___. | do | can | am | 1 | Repeat can in the short answer.
The short form of cannot is: | cann't | cant's | can't | 2 | Can't is the standard contraction.
Choose an ability statement. | I can ride a bike. | My bike is red. | There is a bike. | 0 | Can ride describes an ability.""",
     "Write three things you can do and two things you cannot do yet."),
unit("s16", "Question words and simple instructions", "A1", "interaction", "Ask for basic information and follow short instructions.",
     "Who asks about a person: Who is she? Where asks about place: Where is the bag? What asks about a thing or information: What is your name? An instruction often starts with the base verb: Open the book. Sit down. Add please to be polite. Don't + base verb gives a negative instruction: Don't run.",
     "Match the missing information: person → who; place → where; name or thing → what. For an instruction, start with the action. Don't touch means do not touch, not touch slowly.",
     """Ask for a person's identity: ___ is she? | Who | Where | When | 0 | Who asks about a person.
Ask for a place: ___ is the book? | Who | Where | How old | 1 | Where asks about location.
Ask for a name: ___ is your name? | Where | Who | What | 2 | What asks for this information.
Which is an instruction? | Open the book, please. | My book is blue. | There is a book. | 0 | The base verb Open begins the instruction.
Don't run means: | Run quickly. | Do not run. | You can run. | 1 | Don't makes a negative instruction.
Choose the polite instruction. | Sit please down you. | You sitting. | Sit down, please. | 2 | Sit down gives the action; please adds politeness.
Which word asks about a thing? | What | Who only | Where only | 0 | What can ask about an object or information.""",
     "Write a short classroom dialogue with one who-question, one where-question and two polite instructions."),
]

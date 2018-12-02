================================================================
========================== Gabo  v0.1 ==========================
================================================================


Gabo is a chatbot written in Python 3.7 using the Thonny IDE.

Gabo v0.1 is the initial release beta. If you encounter any 
bugs, please report them to gabo.chatbot@gmail.com

Thank you to all my beta testers for being a part of the Gabo
development project.

Gabo is Copyright (c) 2018 by Jacob Branch, and is licensed for 
free use under the MIT License. See LICENSE.txt for details.

CRITICAL NOTE:
Gabo will only work if the accompanying gabo_vocabulary.json 
file is in the same folder.

Cheers,
J. Branch


================================================================
=========================== Contents ===========================
================================================================

-How to Train Gabo

-How Gabo Works

-Commands

-FAQ

-License

-Changelog

================================================================
====================== How to Train Gabo =======================
================================================================


Gabo is trained through conversation with the user. When you
load gabo for the first time, this is what you will see:


===================== Welcome to Gabo v0.1 =====================

If you are new to Gabo, please read the README.txt or type /help

Say something...

User:


Type in a sentence under User: and hit enter. Your sentence can 
be anything, for example exclamation, statement, question, or 
even a single word. 

For this example, we'll use a greeting.


User:
Hello there.


Now Gabo will respond.


User:
Hello there.

          Gabo:
          hello

 
So far so good, but remember that this is a conversation. We 
should keep going. Let's ask Gabo how it's doing.


User:
How are you?

          Gabo:
          hello


That doesn't make much sense as a response to "How are you?" 
This is because when you first start training Gabo (or after a 
reset), Gabo only knows one word, "hello."

Luckily, we can correct any of Gabo's responses that don't make 
sense with a simple command.

After the last input, our screen looked like this:


User:
How are you?

          Gabo:
          hello

User:


If we want to replace "hello", we can simply type "//" and then 
type the corrected response.


User:
How are you?

          Gabo:
          hello

User:
//I'm fine, thanks.


After we enter this corrected response, it is saved to Gabo's
vocabulary. Gabo then displays the corrected conversation:

User:
How are you?

          Gabo:
          hello

User:
//I'm fine, thanks.

User:
How are you?

          Gabo:
          I'm fine, thanks.


Gabo has learned a new response, and linked it to the question
"How are you?" Lets keep going.


User:
What's your name?

          Gabo:
          I'm fine, thanks.

Whoops, looks like another mismatched answer. Gabo recognized
the sentence as a question, but it only knows one answer to 
questions. Let's teach it some more.

User:
What's your name?

          Gabo:
          I'm fine, thanks.

User:
//My name is Gabo.

User:
What's your name?

          Gabo:
          My name is Gabo.

User:
Hello there, Gabo.

          Gabo:
          hello


Now we're getting somewhere! Notice how Gabo knew to respond
with "hello" when you said "Hello there, Gabo." Let's take a 
look at how Gabo works to understand why.


================================================================
======================== How Gabo Works ========================
================================================================


As I mentioned before, Gabo begin with a vocabulary of one word,
"hello." Every time you type a sentence under User:, Gabo reads,
analyses, and stores it into its vocabulary. It does this for
any corrected responses too, but these get stored in a separate
location within the vocabulary. Each new user sentence and Gabo
response you enter increases the size of its vocabulary and 
allows Gabo to have more variety in its conversation.

When responding to sentence, it first reads what you, the user, 
said (which we'll call the user prompt) and compares it to all
of the other user prompts it's been told before. It is looking
for user prompts with words, phrases, and punctuation in common
with the prompt you just typed.

When it finds the best match, it looks at how you responded to
that matching user prompt, and repeats that response. It then
creates a link between the response and the user prompt inside
the vocabulary's "metadata."

This is what happened when we prompted Gabo with the question
"What's your name?" Gabo read this prompt and searched its
vocabulary for a match. At this point, Gabo had been taught the
following prompts: "Hello there." and, "How are you?" The prompt 
"What's your name?" doesn't have any words in common with either
of these, so Gabo looked for punctuation instead.

Since "What's your name?" has a question mark, Gabo determined
that the user prompt "How are you?" was the best match, and it
responded with the same response, "I'm fine, thanks."

When we corrected this response to "My name is Gabo." Gabo 
stored this sentence in its vocabulary as a new response and
overwrote old the link to the prompt, "What's your name?" This
means that whenever Gabo is asked "What's your name?" (or a 
similar prompt) again, it will respond with "My name is Gabo."

This can help us understand how Gabo knew to respond our last 
prompt, "Hello there, Gabo." with the appropriate response, 
"hello." Let's look at all of the user prompts and their linked 
responses up to this point:

Hello there.      >> hello
How are you?      >> I'm fine, thanks.
What's your name? >> My name is Gabo.

"Hello there." has two words in common and matching punctuation.
That makes it the best match for "Hello there, Gabo." so Gabo
guessed that "hello" was the best fit. Good work, Gabo!

As you train Gabo, it gets better and better at making these
judgements. With enough time, the conversation can start to feel 
natural, with fewer corrections. Eventually, Gabo might even
surprise you with some unexpectedly witty or bizarrely 
appropriate response.

How will your Gabo turn out? Will it have personality? or wit?
or sass? Will it be smart? or socially awkward? You have to 
train it to find out!


================================================================
=========================== Commands ===========================
================================================================


The Gabo console has a number of inbuilt commands to control the
behind the scenes aspects of training your Gabo.

List of user commands:

"/correct" or "//"     = Correct last bot response.
"/prompt"              = Correct last user prompt.
"/save"                = Save current session. (Used if autosave 
			 it disabled.)
"/end" or "/exit"      = End session and exit program. (User 
			 will be prompted to save.)
"/reset"               = Resets the vocabulary database to its 
			 initial blank slate. (Warning: This 
			 cannot be undone.)
"/print" or "/vocab"   = Print the vocabulary database.
			 (Warning: The database file can get 
			 very large, printing may cause crash.)
"/stats"               = Prints statistics from the vocabulary 
			 database.
"/auto"                = Enable/disable autosave. (Autosave is 
			 enabled by default.)
"/bot"                 = Rename Gabo.
"/user"                = Rename User.
"/help" or "/?"        = Get help with Gabo/FAQ.
"/list" or "/commands" = Print a list of user commands.

================================================================


================================================================
============================= FAQ ==============================
================================================================


What is Gabo?

Gabo is a chatbot. This means it is software that can carry on a
conversation. With proper training, a user can teach Gabo a very
large vocabulary. Before long, conversations with Gabo start to 
flow very naturally. If you train Gabo long enough, it may even
surprise you!

================================================================

Is Gabo open-source?

Yes. Gabo's code is open source.

================================================================

Can I modify/adapt Gabo?

Yes. Gabo is licensed under the MIT License. See LICENSE.txt for
details.

================================================================

Is Gabo male or female?

Gabo has no assigned gender. It can, however, be trained to 
identify as any gender the user chooses.

================================================================

Where did Gabo get its name?

Gabo is named after the brilliant Colombian novelist and Nobel 
laureate, Gabriel García Márquez. If you haven't read his works,
go buy and read "One Hundred Years of Solitude" right now. Trust 
me. It's much better written than this README.

================================================================

Can I change Gabo's name?

Yes. Enter the command /bot to change Gabo's name. You can also
change your name from the generic "User" by using the /user
command.

================================================================


================================================================
========================= MIT License ==========================
================================================================


Copyright (c) 2018 Jacob Branch

Permission is hereby granted, free of charge, to any person 
obtaining a copy of this software and associated documentation 
files (the "Software"), to deal in the Software without 
restriction, including without limitation the rights to use, 
copy, modify, merge, publish, distribute, sublicense, and/or 
sell copies of the Software, and to permit persons to whom the 
Software is furnished to do so, subject to the following 
conditions:

The above copyright notice and this permission notice shall be 
included in all copies or substantial portions of the Software.
 
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, 
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES 
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING 
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR 
OTHER DEALINGS IN THE SOFTWARE.


================================================================
========================== Changelog ===========================
================================================================

v0.1

Initial release

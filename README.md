# WELCOME TO MAKING YOUR OWN CHATBOT ON DISCORD 101 (or something)

Making a chatbot requires hardwork and dedication and perspiration. It requires you to be a super coder and be a python guru. It needs to squeeze out every drop of your mathematical skills. Yeah, it's REALLLLLLYYYYY scary. Ahem. Anyways. Here's how to make a chatbot in like 15 minutes or something using python. 

## Dependencies.

Making anything (almost) in python will require you to install some python dependencies. This is code wriiten by amazing people for you to use. No, it's not "cheating". Using other people's software is totally alright because without pre-written code, you're going to be having a tough time coding. These people make things for us easier and no, they don't make you a bad coder. (If anything, knowing about these amazing things makes you better at python).

So for this project, we'll need 4 "dependencies".
- chatterbot==1.0.2
- chatterbot-corpus
- pytz
- discord

### What is ChatterBox?
It's a really cool set of pre-written code that we'll use to train our bot. Yes, train. This is AI, yo. Artificial Intelligence always needs training. Chatterbot helps us provide the right tools to train our bot super easily. Speaking of training, we need data to train our bot. That data is provided by `chatterbot-corpus`. A corpus is a collection of text. This text will go into our bot and our bot will read all of this and learn from it. (It doesn't need 10 years old schooling, no)

### What is discord?
Discord! Your favourite messaging app has a python dependancy package. This is basically `discord.py` (google it!). It's set of pre-written code by Discord for us to interact with discord with code and and andddddd make botsssss! So we'll make our chatbot on discord using discord (or discord.py).

### How do I install these?
It. Is. Simple. Just go to your terminal and typeeee:
```py
pip install <DEPENDENCY>
```

Okay we're set.

![All set](https://media.giphy.com/media/TwmEnGgxdUT4Y/giphy.gif)

##Getting Started

To make it easier for us to start, I have written some code already. 

1. Open the `main.py` file.
2. You'll see this code there:
```py
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name="MyBot", 
                read_only=True,
                logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])
```
   This code imports a bunch of stuff and initalises your bot. This means that after this code, your bot ACTUALLY EXISTS in your code. We always do this in python.
3. The next lines are data that we'll give to our bot to learn. Our bot is going to read this data and learn from it (in literally seconds).
```py
small_talk = [
  "yo",
  "HELLO!",
  "how's life",
  "Life's good",
  "Goodbye!",
  "Bye bye!"
]

math_talk = [
  "Pythagoras' theorm",
  "A squared plus b squared is equal to c squared"
]

list_trainers = ListTrainer(my_bot)
for item in (small_talk, math_talk):
  list_trainers.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
```
4. Now that our bot is well read and well educated. It's time for it to go out there and live its life. Now is the time. This code will actually make your bot take input and give out output.
```py
while True:
  bot_input = input("You: ")
  bot_response = my_bot.get_response(bot_input)
  print(f"{my_bot.name}: {bot_response}")
```
5. AAAAND you're done. See, I told you it'll be hard.

![yayyyyyyyyy](https://media.giphy.com/media/jd6TVgsph6w7e/giphy.gif)


## Wait... this isn't discord-

Yes, I know, dummy. NOW is the discord part. You've done well, padawan. Now open the next file `discordBot.py`. I have some secret already-written code for you there.

1. So this code is, actually, of a complete discord bot. It goes:
```py
import discord
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

client = discord.Client()

my_bot = ChatBot(name="MyBot", 
                read_only=True,
                logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"])

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')
```

   You'll notice some code from our previous program. This IS actually a whole discord bot which will say "Hello!" if you say "$hello". The "your token here" is where you secret token goes that you got while making this discord bot on their website.
2. Now the task remains to merge our previously made AI chatbot to this discord bot. HMMMMMHHHHH. Okay, let's try THIS:
```py
small_talk = [
  "yo",
  "HELLO!",
  "how's life",
  "Life's good",
  "Goodbye!",
  "Bye bye!"
]

math_talk = [
  "Pythagoras' theorm",
  "A squared plus b squared is equal to c squared"
]

list_trainers = ListTrainer(my_bot)
for item in (small_talk, math_talk):
  list_trainers.train(item)

corpus_trainer = ChatterBotCorpusTrainer(my_bot)
corpus_trainer.train('chatterbot.corpus.english')
```
   How about training our bot like we did? I mean, training shouldn't be any different, right? Yeah, this looks fine. Our bot is all grown up.
3. The final step. ACTUALLY making our bot say something in the discord server. Here, we'll just modify our last code a little to make it more "discord".
```py
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
     
    bot_input = message.content
    bot_response = my_bot.get_response(bot_input)
    await message.channel.send(bot_response)

```
   ta daaaaaaa! This is just both the code merged. We took the discord async function `on_message` which does something when the user messages. What does it do? It take the `message.content` which is whatever was IN that text that the user just sent on the server and puts it into the variable `bot_input`. After this, it asks our AI bot to generate some response and store it in the variable `bot_response`. Finally, we just sent this variable as a text to whatever channel was open in the discord server. There. Done.
4. And we've done it once againnn!

![we winnnn!](https://media.giphy.com/media/3o7ZeTmU77UlPyeR2w/giphy.gif)

## We are done!

We're done. Yes, sahi mein. Try it. Play with your bot. However, you SHOULDDDDDD remember that with great power comes great responsibility. Nah, I'm just kidding. Go nuts. But but but this is just the VERY VERY basic of AI and bot making on python. With this knowledge you can go ahead and do other cool stuff with it. Only your imagination is the limit. You have your own discord bot now, your own AI chatbot and your fresh python skills. Well done!

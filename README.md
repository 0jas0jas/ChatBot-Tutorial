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

1. 

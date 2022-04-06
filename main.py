from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name="MyBot", 
                read_only=True,
                logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
                )

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

while True:
  bot_input = input("You: ")
  bot_response = my_bot.get_response(bot_input)
  print(f"{my_bot.name}: {bot_response}")

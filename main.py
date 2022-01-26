from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot(name="MyBot", 
                read_only=True,
                logic_adapters=["chatterbot.logic.MathematicalEvaluation", "chatterbot.logic.BestMatch"]
                )

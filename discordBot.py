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

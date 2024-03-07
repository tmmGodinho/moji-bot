import discord
import random
from dotenv import load_dotenv
import os
import datetime


# IMPLEMENT GOODBYE I SLEEP MESSAGE
# CTRL+/ para comentar blocos

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    # corre procedimento 
    await go_count()
    # channel = client.get_channel(297815778084782081)
    # await channel.send("<@196422847818629120> you're next")

async def go_count():
    channel = client.get_channel(1214006594090565642)
    how_many_mojis = 0
    word = "💩"
    async for message in channel.history():
        if word in message.content:
            how_many_mojis += 1
    print(f"We have collectively 💩 {how_many_mojis} times. Great job.")




@client.event
async def on_message(message):
    print(message)

    # if message.author.name == "chibanga":
    #     await message.reply("Sou capaz de responder a mensagens ;)")

    if message.author.name == "ponei_lider":
        attack_girao_prob = random.random()
        print(attack_girao_prob)
        if attack_girao_prob < .25:
            await message.reply("Calado eras poeta")
        
        #await message.channel.send('Calado eras poeta')

    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

#make this run from system variable instead of having the key here 
#bot_key = os.environ['BOT_KEY']
bot_key = os.getenv("BOT_KEY")
client.run(bot_key)

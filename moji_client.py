import discord

class MojiClient(discord.Client):
    
    def __init__(self):
        # TODO: GET EMOJI FROM .ENV
        # self.emoji = "💩"
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)

import discord
import random

class MojiClient(discord.Client):
    moji_dict = {}
    ranking = 'Hello. This is a test of the ranking feature\n'
    
    def __init__(self):
        # TODO: GET EMOJI FROM .ENV
        self.emoji = "💩"
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)

    # @client.event
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        # corre procedimento 
        await self.go_count()
        # channel = client.get_channel(297815778084782081)
        # await channel.send("<@196422847818629120> you're next")

    async def go_count(self):
        channel = self.get_channel(1214006594090565642)
        await self.parse_moji()
        self.go_rank()
        ranking = self.make_string()
        await self.go_post(channel)


    async def parse_moji(self):
        how_many_mojis = 0
        channel = self.get_channel(1214006594090565642)
        async for message in channel.history():
            if self.emoji in message.content:
                if message.author.id in self.moji_dict.keys():
                    self.moji_dict[message.author.id] += 1
                    how_many_mojis += 1
                else:
                    self.moji_dict[message.author.id] = 1
                    how_many_mojis += 1              
        print(f"We have collectively 💩 {how_many_mojis} times. Great job.")
        print(self.moji_dict)

    def go_rank(self):
        self.moji_dict = dict(sorted(self.moji_dict.items(), key=lambda item: item[1], reverse=True))
        

    def make_string(self):
        place = 1
        for key in self.moji_dict:
            match place:
                case 1:
                    self.ranking += f":first_place: <@{key}> > {self.moji_dict[key]}\n"
                case 2:
                    self.ranking += f":second_place: <@{key}> > {self.moji_dict[key]}\n"
                case 3:
                    self.ranking += f":third_place: <@{key}> > {self.moji_dict[key]}\n"
                case _:
                    self.ranking += f"#{place}:<@{key}> > {self.moji_dict[key]}\n"
            place += 1
        print(self.ranking)
        


    async def go_post(self, channel):
        print(self.ranking)
        #embed=discord.Embed(title="Test Embed", description=ranking, color=discord.Color.random())
        #await channel.send(embed=embed)


    async def on_message(self, message):
        print(message)
        if message.author.name == "ponei_lider":
            attack_girao_prob = random.random()
            print(attack_girao_prob)
            if attack_girao_prob < .25:
                await message.reply("Calado eras poeta")
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!')    
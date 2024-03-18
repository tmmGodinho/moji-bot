import discord
import random
from datetime import datetime



class MojiClient(discord.Client):
    moji_dict = {}
    ranking = ''
    


    def __init__(self, emoji):
        # TODO: GET EMOJI FROM .ENV
        self.emoji = emoji
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)

    # @client.event
    async def on_ready(self):
        print(f'We have logged in as {self.user}')

        await self.go_count()
        # await channel.send("<@196422847818629120> you're next") /dd

    async def go_count(self, last_month = False):
        channel = self.get_channel(1214006594090565642)
        await self.parse_moji()
        self.go_rank()
        ranking = self.make_string()
        await self.go_post(channel)


    async def parse_moji(self):
        channel = self.get_channel(1214006594090565642)
        day_today = datetime.today()
        print("datetime is :", day_today)
        day_one = day_today.replace(day = 1, hour = 0, minute = 0, second = 0)
        print("first day of the month", day_one)
        await self.fill_ranking(channel, day_one)
        print(self.moji_dict)

    async def fill_ranking(self, channel, day_one, final_day = False):
        how_many_mojis = 0
        async for message in channel.history(after = day_one):
            if self.emoji in message.content:
                if message.author.id in self.moji_dict.keys():
                    self.moji_dict[message.author.id] += 1
                    how_many_mojis += 1
                else:
                    self.moji_dict[message.author.id] = 1
                    how_many_mojis += 1  
        print(f"We have collectively 💩 {how_many_mojis} times. Great job.")

    def go_rank(self):
        self.moji_dict = dict(sorted(self.moji_dict.items(), key=lambda item: item[1], reverse=True))
        

    def make_string(self):
        self.ranking = 'Hello. This is a test of the ranking feature\n'
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

    def go_last_month():
        pass



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
            await message.channel.send('Hello!') & message.channel == 1214006594090565642   
        if message.content.startswith('$lastmonth'):
            self.go_last_month() 
            
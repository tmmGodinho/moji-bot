import discord
import random
from datetime import datetime



class MojiClient(discord.Client):
    moji_dict = {}
    ranking = ''
    moji_channel = None


    def __init__(self, emoji, channel_id):
        self.emoji = emoji
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents = intents)
        self.channel_id = channel_id
        

    async def on_ready(self):
        print(f'We have logged in as {self.user}')
        self.moji_channel = self.get_channel(self.channel_id)
        await self.go_count()

    async def go_count(self, last_month = False):
        await self.parse_moji()
        self.go_rank()
        ranking = self.make_string()
        await self.go_post()


    async def parse_moji(self, last_month = False):
        day_today = datetime.now()
        print("datetime is :", day_today)
        day_one = day_today.replace(day = 1, hour = 0, minute = 0, second = 0)
        print("first day of the month", day_one)
        if(last_month != False):
            final_day = day_one.replace(month = final_day.month-1)
            await self.fill_ranking(day_one, final_day=final_day)
        else:
            await self.fill_ranking(day_one)
        print(self.moji_dict)

    async def fill_ranking(self, day_one, final_day = False):
        how_many_mojis = 0
        if(final_day == False):
            final_day = datetime.now()
        else:
            pass
        async for message in self.moji_channel.history(after = day_one, before = final_day, limit = 10000):
            if self.emoji in message.content:
                if message.author.id in self.moji_dict.keys():
                    self.moji_dict[message.author.id] += 1
                else:
                    self.moji_dict[message.author.id] = 1
                how_many_mojis += 1      
        print(f"We have collectively {self.emoji} {how_many_mojis} times. Great job.")

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


    async def parse_last_month(self):
        self.moji_dict = {}
        day_today = datetime.now()
        print("datetime is :", day_today)
        day_one = day_today.replace(day = 1, hour = 0, minute = 0, second = 0)
        print("first day of the month", day_one)
        day_one_last_month = day_one.replace(month=day_one.month-1)
        print("first day of the last month", day_one_last_month)
        await self.fill_ranking(day_one_last_month, day_one)
        print(self.moji_dict)
        


    async def go_post(self):
        print(self.ranking)
        #embed=discord.Embed(title="Test Embed", description=ranking, color=discord.Color.random())
        #await self.moji_channel.send(embed=embed)

    async def go_last_month(self):
        await self.parse_last_month()
        self.go_rank()
        ranking = self.make_string()
        await self.go_post()



    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith('$hello'):
            await message.channel.send('Hello!') 
        if message.content.startswith('$lastmonth'):
            await self.go_last_month() 
            
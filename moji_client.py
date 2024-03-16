import discord
import random

class MojiClient(discord.Client):
    
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
        moji_dict = {}
        ranking = 'Hello. This is a test of the ranking feature\n'
        await self.parse_moji(moji_dict)
        ranking = self.go_rank(moji_dict, ranking)
        await self.go_post(moji_dict, ranking, channel)

        # embed=discord.Embed(title="Test Embed", description=ranking, color=discord.Color.random())
        # await message.channel.send(embed=embed)



    async def parse_moji(self, moji_dict):
        how_many_mojis = 0
        channel = self.get_channel(1214006594090565642)
        async for message in channel.history():
            if self.emoji in message.content:
                if message.author.id in moji_dict.keys():
                    moji_dict[message.author.id] += 1
                    how_many_mojis += 1
                else:
                    moji_dict[message.author.id] = 1
                    how_many_mojis += 1              
        print(f"We have collectively 💩 {how_many_mojis} times. Great job.")
        print(moji_dict)

    def go_rank(self, moji_dict, ranking):
        ordered_list = dict(sorted(moji_dict.items(), key=lambda item: item[1], reverse=True))
        place = 1
        for key in ordered_list:
            match place:
                case 1:
                    ranking += f":first_place: <@{key}> > {ordered_list[key]}\n"
                case 2:
                    ranking += f":second_place: <@{key}> > {ordered_list[key]}\n"
                case 3:
                    ranking += f":third_place: <@{key}> > {ordered_list[key]}\n"
                case _:
                    ranking += f"#{place}:<@{key}> > {ordered_list[key]}\n"
            place += 1
        print(ranking)
        return ranking


    async def go_post(self, moji_dict, ranking, channel):
        print(ranking)
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
import discord
from datetime import datetime
from dateutil.relativedelta import relativedelta


class MojiClient(discord.Client):
    moji_channel = None

    def __init__(self, emoji, channel_id):
        self.emoji = emoji
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(intents=intents)
        self.channel_id = channel_id

    async def on_ready(self):
        self.moji_channel = self.get_channel(self.channel_id)
        await self.go_count()

    async def go_count(self, is_last_month=False):
        start_ds, end_ds = MojiClient.gen_date_range(is_last_month)
        moji_dict = await self.fill_ranking(start_ds, end_ds)
        moji_dict = self.go_rank(moji_dict)
        ranking_msg = self.make_string(moji_dict)
        await self.go_post(ranking_msg)

    async def fill_ranking(self, start_ds, end_ds):
        moji_dict = {}
        how_many_mojis = 0
        async for message in self.moji_channel.history(
            after=start_ds, before=end_ds, limit=10000
        ):
            if self.emoji in message.content:
                if message.author.id in moji_dict.keys():
                    moji_dict[message.author.id] += 1
                else:
                    moji_dict[message.author.id] = 1
                how_many_mojis += 1
        return moji_dict

    def make_string(self, moji_dict):
        if not moji_dict:
            return f"There are no {self.emoji} to rank yet!"
        place = 1
        ranking_msg = "Hello. These are the ranking results: \n"
        for key in moji_dict:
            match place:
                case 1:
                    ranking_msg += f":first_place: <@{key}> > {moji_dict[key]}\n"
                case 2:
                    ranking_msg += f":second_place: <@{key}> > {moji_dict[key]}\n"
                case 3:
                    ranking_msg += f":third_place: <@{key}> > {moji_dict[key]}\n"
                case _:
                    ranking_msg += f"#{place}:<@{key}> > {moji_dict[key]}\n"
            place += 1
        return ranking_msg

    async def go_post(self, ranking_msg):
        embed = discord.Embed(
            title=f"{self.emoji} Ranking",
            description=ranking_msg,
            color=discord.Color.random(),
        )
        await self.moji_channel.send(embed=embed)

    async def on_message(self, message):
        if message.author == self.user:
            return
        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")
        if message.content.startswith("$lastmonth"):
            await self.go_count(True)

    @staticmethod
    def gen_date_range(is_last_month):
        day_today = datetime.now()
        day_one = day_today.replace(day=1, hour=0, minute=0, second=0)
        if is_last_month:
            start_ds = day_one - relativedelta(months=1)
            end_ds = day_one
        else:
            start_ds = day_one
            end_ds = day_today
        return start_ds, end_ds

    @staticmethod
    def go_rank(moji_dict):
        return dict(sorted(moji_dict.items(), key=lambda item: item[1], reverse=True))

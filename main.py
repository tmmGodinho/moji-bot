from dotenv import load_dotenv
import os
from moji_client import MojiClient


# TODO set exception for tie in ranking
# TODO insert month variable into ranking message

load_dotenv()
emoji = os.getenv("MOJI")
channel = int(os.getenv("CHANNEL"))
client = MojiClient(emoji, channel)

bot_key = os.getenv("BOT_KEY")
client.run(bot_key)

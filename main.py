from dotenv import load_dotenv
import os
from moji_client import MojiClient


# IMPLEMENT GOODBYE I SLEEP MESSAGE
# CTRL+/ para comentar blocos


#TODO implement datetime filter on message get

load_dotenv()
emoji = os.getenv("MOJI")
channel = int(os.getenv("CHANNEL"))
client = MojiClient(emoji, channel)


bot_key = os.getenv("BOT_KEY")
client.run(bot_key)

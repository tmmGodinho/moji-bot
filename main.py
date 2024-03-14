import discord
import random
from dotenv import load_dotenv
import os
import datetime
from moji_client import MojiClient


# IMPLEMENT GOODBYE I SLEEP MESSAGE
# CTRL+/ para comentar blocos

#TODO on class init, call a new method: parse historical messages. This should populate class variables
#TODO inside of class, create a gen_message method that returns the message you want to send. It should use the class variables defined through your init logic
#TODO call format from your event method that will trigger it
#TODO run it cleanly from your main.py file
#TODO implement datetime filter on message get
#TODO refactor message get
#TODO refactor string build

load_dotenv()
client = MojiClient()

#make this run from system variable instead of having the key here 
#bot_key = os.environ['BOT_KEY']
bot_key = os.getenv("BOT_KEY")
client.run(bot_key)

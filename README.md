# moji-bot
Counts and ranks amount of monthly emoji usage in a specific discord channel.

On startup, moji-bot will count and rank the current month's specified emoji usage on a specified discord  channel. It also makes use of a chat command, $lastmonth, in which moji-bot counts and ranks last month's emoji usage. This project is meant as a personal refresher for python, while also exploring and making use of discord.py.

# Setup
Before moji-bot can operate, you will have to fill out the parameters in your .env file. The parameters are as follows:

-BOT_KEY: This is your bot's private key, and as such should be treated as very sensitive information. Do not share with anyone. You can find more details on how to get this [here](https://www.writebots.com/discord-bot-token/)

-MOJI: The emoji you want to rank. This works with actual emojis (you can search for emojis on windows using the 'WIN+.' shortcut)

-CHANNEL: The channel id for the channel in which you want moji-bot to operate.

# Running
Run main.py 

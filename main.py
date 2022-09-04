import os
import json
import discord
from discord.ext import commands

with open('config.json', 'r') as f:
    config = json.load(f)

cmd_prefix = config["cmd_prefix"]
token_main = config["token_main"]

bot_intents = discord.Intents.all()

my_bot = commands.Bot(
    intents = bot_intents, 
    command_prefix = commands.when_mentioned_or(cmd_prefix)
)

my_bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        my_bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'"{filename[:-3]}" загружен')


my_bot.run(token_main)

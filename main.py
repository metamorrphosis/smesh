import os
import json
import config
import discord
from discord.ext import commands

bot_intents = discord.Intents.all()

my_bot = commands.Bot(
    intents = bot_intents, 
    command_prefix = commands.when_mentioned_or(config.cmd_prefix)
)

my_bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        my_bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'"{filename[:-3]}" загружен')


my_bot.run(config.token_main)

import os
import json
import config
import discord
from datetime import datetime
from discord.ext import commands


class MyContext(commands.Context):  
    async def error(self, *, title = '❌ Ошибка', description = None, fields = None):
        emberror = discord.Embed(
            title = title,
            color = 0xf03a3a,
            timestamp = datetime.now(),
            description = description,
            fields = fields
        )
        emberror.set_footer(text = self.author, icon_url = self.author.display_avatar.url)
        await self.reply(embed = emberror)

    async def success(self, *, title = 'Успешно', description = None, fields = None):
        emberror = discord.Embed(
            title = title,
            color = 0x9cde6e,
            timestamp = datetime.now(),
            description = description,
            fields = fields
        )
        emberror.set_footer(text = self.author, icon_url = self.author.display_avatar.url)
        await self.reply(embed = emberror)

    async def natural(self, *, title = None, description = None, fields = None):
        emberror = discord.Embed(
            title = title,
            color = 0xbffed9,
            timestamp = datetime.now(),
            description = description,
            fields = fields
        )
        emberror.set_footer(text = self.author, icon_url = self.author.display_avatar.url)
        await self.reply(embed = emberror)

class MyBot(commands.Bot):
    async def get_context(self, message: discord.Message, *, cls = MyContext):
        return await super().get_context(message, cls = cls)
   
bot_intents = discord.Intents.all()

my_bot = MyBot(
    intents = bot_intents, 
    command_prefix = commands.when_mentioned_or(config.cmd_prefix)
)
my_bot.remove_command('help')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        my_bot.load_extension(f'cogs.{filename[:-3]}')
        print(f'"{filename[:-3]}" загружен')


my_bot.run(config.token_main)

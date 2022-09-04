import os
import json
import config
import pymongo
import discord
from discord.ext import commands
from datetime import datetime


# cluster = pymongo.MongoClient("mongodb+srv://bebroidik:okBL9W7DABgfpqhf@cluster0.7wcrgyr.mongodb.net/?retryWrites=true&w=majority")
# db = cluster["cluster0"] # название кластера, не меняй его
# collection = db["uptime"] # название колекции, не меняй его

class Start(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        # dtint = datetime.timestamp(datetime.now())
        # collection.update_one({"_id": 0}, {"$set": {"uptime": int(dtint)}})
        botping = int(self.bot.latency * 1000)
        await self.bot.change_presence(activity=discord.Game(name=f"{config.cmd_prefix}"), status = discord.Status.dnd)
        print(f'{self.bot.user} | {self.bot.user.id} запущен\n\nКоличество выгруженных файлов: {len(self.bot.extensions)}, когов: {len(self.bot.cogs)}\nПинг бота: {botping} мс\n------------------------')
        
def setup(bot):
    bot.add_cog(Start(bot))

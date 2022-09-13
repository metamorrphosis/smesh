import config
import discord
from discord.ext import commands

class StartCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        botping = int(self.bot.latency * 1000)
        await self.bot.change_presence(activity=discord.Game(name=f"{config.cmd_prefix}"), status = discord.Status.dnd)
        print(f'{self.bot.user} | {self.bot.user.id} запущен\n\nКоличество выгруженных файлов: {len(self.bot.extensions)}, когов: {len(self.bot.cogs)}\nПинг бота: {botping} мс\n------------------------')
        
def setup(bot):
    bot.add_cog(StartCog(bot))

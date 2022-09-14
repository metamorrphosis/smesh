import discord
from utils import economy_db
from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = economy_db.EconomyDB()

    @commands.command(aliases = ['money', 'bal', 'бал', 'баланс'])
    async def balance(self, ctx):
        member_bal = await self.db.get_money(member = member)
        print(member_bal)
        
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
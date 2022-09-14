import discord
from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def test(self, ctx):
        await ctx.error()
        await ctx.success()
        await ctx.natural()
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
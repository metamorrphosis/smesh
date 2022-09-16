import discord
from discord.ext import commands

class AutoRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def emoji(self, ctx):
        await ctx.channel.purge(limit = 200)
        for i in ctx.guild.emojis:
            await ctx.send(i)
            await ctx.send(f'\{i}')
    
def setup(bot):
    bot.add_cog(AutoRolesCog(bot))
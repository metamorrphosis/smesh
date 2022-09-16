import discord
from discord.ext import commands

class AutoRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def emoji(self, ctx):
        if ctx.guild.id != 1018511272196722760:
            return
    
        await ctx.channel.purge(limit = 200)

        for i in ctx.guild.emojis:
            await ctx.send(i)
            await ctx.send(f'\{i}')
    
def setup(bot):
    bot.add_cog(AutoRolesCog(bot))
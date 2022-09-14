import discord
from discord.ext import commands

class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def url(self, ctx):
        m = await ctx.channel.fetch_message(1019628854748393483)
        s = m.embeds[0].fields[0].value
        e = discord.PartialEmoji.from_str(s)
        await ctx.message.reply(e.url)
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
import discord
from discord.ext import commands
from datetime import datetime, timedelta


class AnticrashCommandsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def bebrocka(self, ctx):
        return 'b'


def setup(bot):
    bot.add_cog(AnticrashCommandsCog(bot))
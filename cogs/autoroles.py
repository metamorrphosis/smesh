import discord
from discord.ext import commands

class AutoRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hook(self, ctx):
        channel = ctx.guild.get_channel(1004655381806600222)
        webhook = await channel.create_webhook(name = 'Smesh')
        await ctx.message.reply(webhook.url)
    
def setup(bot):
    bot.add_cog(AutoRolesCog(bot))
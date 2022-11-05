import discord
from discord.ext import commands
import config
from utils.other import auto_role

class AutoRolesView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_news:1018512472761708604>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "news_role_button"
    )
    async def news_role_callback(self, button, interaction):
        result = await auto_role(interaction.user, interaction.guild.get_role(993099769843040286))
        await interaction.response.send_message(result, ephemeral = True)
    

    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_party:1018512458538815528>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "games_role_button"
    )
    async def games_role_callback(self, button, interaction):
        result = await auto_role(interaction.user, interaction.guild.get_role(993099923711078491))
        await interaction.response.send_message(result, ephemeral = True)
    
    
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_gift:1018512394391146597>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "giveaways_role_button"
    )
    async def giveaways_role_callback(self, button, interaction):
        result = await auto_role(interaction.user, interaction.guild.get_role(993104348982820924))
        await interaction.response.send_message(result, ephemeral = True)


class AutoRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True)
    async def ar(self, ctx):
        embroles = await ctx.channel.history(limit = 100).flatten()
        embroles = embroles[1]
        embroles = embroles.embeds
        await ctx.message.delete()
        channel = ctx.guild.get_channel(config.autoroles_channel)
        webhook = await channel.webhooks()
        webhook = webhook[0]

        await webhook.send(embeds = embroles, view = AutoRolesView())
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(AutoRolesView())


def setup(bot):
    bot.add_cog(AutoRolesCog(bot))

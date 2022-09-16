import discord
from discord.ext import commands
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


class AutoRolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True)
    async def ar(self, ctx):
        embroles = [
            discord.Embed(
                title = '<:e_green_list:1018821075926253568>・Роли оповещений',
                description = '━────────────────━\n<:a_news:1018512472761708604><:e_white_dot:1018821114853601353><@&993099769843040286> - Оповещения о событиях на сервере.\n\n<:a_party:1018512458538815528><:e_green_dot:1018821297481994280><@&993099923711078491> - Оповещения игровых мероприятий на сервере.\n\n<:a_gift:1018512394391146597><:e_white_dot:1018821114853601353><@&993104348982820924> - Оповещения о розыгрышах на сервере.',
                color = 0xbffed9
            )
        ]

        embroles[0].set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')

        await ctx.message.delete()
        channel = ctx.guild.get_channel(1004655381806600222)
        webhook = await channel.webhooks()
        webhook = webhook[0]

        await webhook.send(embeds = embroles, view = AutoRolesView())
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(AutoRolesView())


def setup(bot):
    bot.add_cog(AutoRolesCog(bot))
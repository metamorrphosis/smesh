import discord
from datetime import datetime
from discord import option
from discord.ext import commands


class SuggestionsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @discord.slash_command(
        name = 'suggestion', 
        description = 'Отправляет ваш заказ ивента в #﹑🐔﹒заказы',
        guild_ids = [837941760193724426],
        guild_only = True
    )
    @option(
        name = 'Ивент',
        description = 'Ивент, который вы хотите заказать',
        input_type = str,
        required = True
    )
    async def suggestion_slash_command(self, ctx, 
        _suggestion: discord.Option(
                                                        name = 'Ивент', 
                                                        required = True, 
                                                        input_type = str, 
                                                        description = 'Ивент, который вы хотите заказать')
    ):
        suggestion_channel = ctx.guild.get_channel(1032609206764847105)
        suggestion_embed = discord.Embed(
            title = '<:a_news:1018512472761708604> Новый заказ ивента',
            color = 0xbffed9,
            timestamp = datetime.now(),
            fields = [
                discord.EmbedField(
                    name = 'Автор заказа',
                    value = f'{ctx.author.mention} | `{ctx.author}` | `{ctx.author.id}`'
                ),
                discord.EmbedField(
                    name = 'Заказ',
                    value = str(_suggestion)
                )
            ]
        )
        suggestion_embed.set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')
        suggestion_message = await suggestion_channel.send(embed = suggestion_embed)
        await suggestion_message.add_reaction('👍')
        await suggestion_message.add_reaction('👎')
        await ctx.send_response('Ваш заказ успешно отправлен в <#1032609206764847105>', ephemeral = True)
        


def setup(bot):
    bot.add_cog(SuggestionsCog(bot))

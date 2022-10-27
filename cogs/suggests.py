import discord
from datetime import datetime
from discord import option
from discord.ext import commands


class SuggestsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.slash_command(
        name = 'suggest', 
        description = 'Отправляет ваш заказ ивента в #﹑🐔﹒заказы',
        guild_only = True
    )
    @option(
        name = 'Ивент',
        description = 'Ивент, который вы хотите заказать',
        input_type = str,
        required = True
    )
    async def suggest_slash_command(self, ctx, _suggest: str):
        suggest_channel = ctx.guild.get_channel(1032609206764847105)
        suggest_embed = discord.Embed(
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
                    value = str(_suggest)
                )
            ]
        )
        suggest_embed.set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')
        await suggest_channel.send(embed = suggest_embed)
        await ctx.send_response('Ваш заказ успешно отправлен в <#1032609206764847105>', ephemeral = True)
        


def setup(bot):
    bot.add_cog(SuggestsCog(bot))

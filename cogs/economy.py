import config
import discord
from typing import Union
from utils import economy_db
from discord.ext import commands
prf = config.cmd_prefix


class EconomyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = economy_db.EconomyDB()

    @commands.command(aliases = ['money', 'bal', 'бал', 'баланс'])
    async def balance(self, ctx, member: discord.Member = None):
        member = member or ctx.author
        member_bal = await self.db.get_money(member = member)
        await ctx.natural(
            title = f'Баланс {member}',
            fields = [
                discord.EmbedField(
                    name = 'Наличные', 
                    value = f'<:vajno_2:1018512718585679882>{member_bal["cash"]}', 
                    inline = True
                ),
                discord.EmbedField(
                    name = 'Банк', 
                    value = f'<:vajno_2:1018512718585679882>{member_bal["bank"]}', 
                    inline = True
                ),
                discord.EmbedField(
                    name = 'Всего', 
                    value = f'<:vajno_2:1018512718585679882>{member_bal["cash"] + member_bal["bank"]}', 
                    inline = True
                )
            ]
        )
    
    @commands.command(aliases = ['add-money', 'выдать-деньги', 'выдатьденьги', 'аддмоней', 'монейадд'])
    async def addmoney(self, ctx, member: discord.Member = None, mode = None, value = None):
        usage_field = discord.EmbedField(
            name = 'Использование команды',
            value = f'`{prf}add-money <ник, упоминание или ID участника> <куда выдать (наличные, банк), если указать тут не режим а число — выдача в банк> [количество, указывать только если указан режим]`',
        )
        examples_field = discord.EmbedField(
            name = 'Примеры использования команды',
            value = f'`{prf}add-money @Петя228 5000` — поскольку вместо режима число — выдаст пете 5000 валюты в банк\
            \n\n`{prf}add-money 1007615585506566205 cash 10,000` — выдаст участнику по ID 10,000 валюты в наличные'
        )

        if member is None:
            return await ctx.error(description = 'Вы не указали участника, которому необходимо выдать валюту', fields = [usage_field, examples_field])
        
        await self.db.add_money(
            member = member,
            mode = "bank",
            value = value
        )
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
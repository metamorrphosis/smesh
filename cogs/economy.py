import config
import discord
from typing import Union
from utils import economy_db
from utils.other import nc
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
    
    @commands.command(aliases = ['add-money', 'am', 'выдать-деньги', 'выдатьденьги', 'аддмоней', 'монейадд'])
    async def addmoney(self, ctx, member: Union[discord.Member, str] = None, mode = None, value = None):
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
            return await ctx.error(description = 'Вы не указали участника, которому необходимо выдать валюту в первом аргументе', fields = [usage_field, examples_field])
        
        if not(isinstance(member, discord.Member)):
            return await ctx.error(description = 'Участник не найден')

        if mode is None:
            return await ctx.error(description = 'Вы не указали режим, куда нужно выдать деньги, либо число в втором аргументе', fields = [usage_field, examples_field])
        
        cash_list = ['cash', 'наличные', 'кеш', 'наличка']
        bank_list = ['bank', 'банк']

        if mode in cash_list:
            mode = 'cash'
        elif mode in bank_list:
            mode = 'bank'
        elif mode.isdigit():
            value = mode
            mode = 'bank'
        else:
            return await ctx.error(description = 'Вы не указали не режим и не положительное число вторым аргументом', fields = [usage_field, examples_field])
        
        if value is None:
            return await ctx.error(description = 'Вы указали режим, и не указали положительное число в третьем аргументе', fields = [usage_field, examples_field])

        if not(value.isdigit()):
            return await ctx.error(description = 'Вы указали не положительное число в третьем аргументе', fields = [usage_field, examples_field])
        
        value = int(value)

        if value >= 1000000000000000000:
            return await ctx.error(description = f'Число не может быть больше {nc("1000000000000000000")}')

        await self.db.add_money(
            member = member,
            mode = mode,
            value = value
        )

        await ctx.success(
            description = f'Выдал {nc(str(value))}<:vajno_2:1018512718585679882> {member.mentiob} (`{member}`) в {"банк" if mode == "bank" else "наличные"}'
        )
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
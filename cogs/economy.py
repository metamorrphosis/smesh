import discord
from utils import economy_db
from discord.ext import commands

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
        
    
def setup(bot):
    bot.add_cog(EconomyCog(bot))
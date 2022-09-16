import config
import discord
from typing import Union
from utils import temp_warns_db
from utils.other import nc
from discord.ext import commands
prf = config.cmd_prefix


class TempWarnsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = temp_warns_db.TempWarnsDB()
    
    @commands.command(aliases = ['устные'])
    async def temp_warns(self, ctx, member: Union[discord.Member, str] = None):
        member = member or ctx.author

        if not(isinstance(member, discord.Member)):
            return await ctx.error(description = 'Участник не найден')
        
        member_temp_warn = await self.db.get_warn(member = member)

        if member_temp_warn is None:
            description = 'Устные отсутсвуют'
        else:
            warn_author_id = member_temp_warn["author"]
            warn_author = ctx.guild.get_member(warn_author_id)

            if warn_author is None:
                warn_author = f'<@{warn_author_id}> (`Данный участник покинул сервер`)'
            else:
                warn_author = f'{warn_author.mention} (`{warn_author}`)'
            
            description = f'**От кого:** {warn_author}\n**Действует до:** <t:{member_temp_warn["duration"]}:f>'
        

        await ctx.natural(
            title = f'Устные {member}',
            description = description
        )


def setup(bot):
    bot.add_cog(TempWarnsCog(bot))
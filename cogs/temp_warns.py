import config
import discord
from typing import Union
from utils import temp_warns_db, my_roles
from utils.other import nc
from discord.ext import commands
prf = config.cmd_prefix


class TempWarnsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = temp_warns_db.TempWarnsDB()
    
    @commands.command(aliases = ['устные', 'уе'])
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
    

    @commands.command(aliases = ['устный'])
    async def temp_warn(self, ctx):
        uroles = my_roles.Roles(ctx.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = ctx.author,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        
        return await ctx.error(f'Эта команда доступна только для следующих ролей:\n {roles_mention}')


def setup(bot):
    bot.add_cog(TempWarnsCog(bot))
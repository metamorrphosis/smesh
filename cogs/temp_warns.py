import config
import discord
from typing import Union
from utils import temp_warns_db, my_roles
from utils.other import nc, get_duration
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
    

    @commands.command(aliases = ['устный', 'уй'])
    async def temp_warn(self, ctx, member: Union[discord.Member, str] = None, duration = None):
        uroles = my_roles.Roles(ctx.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = ctx.author,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await ctx.error(description = f'Эта команда доступна только для следующих ролей:\n {roles_mention}')
        
        if isinstance(member, discord.Member):
            if duration is None:
                return await ctx.error(description = 'Вы не указали время устного во втором аргументе')
        elif ctx.message.reference is not None:
            if member is None:
                return await ctx.error(description = 'Вы не указали время устного во первом аргументе')
            duration = member
            member = ctx.message.reference.resolved.author
        else:
            return await ctx.error(description = 'Участник не найден. Вы должны указать ник, упоминание или ID участника первым сообщением, либо ответить на сообщение того, кому нужно выдать устный')

        if member.id == ctx.author.id:
            return await ctx.error(description = 'Нельзя выдать устный себе')
        
        if member.bot:
            return await ctx.error(description = 'Нельзя выдать устный боту')
        
        if member.top_role.position >= ctx.author.top_role.position:
            return await ctx.error(description = 'Нельзя выдать мьют участнику, который находится на одной роли с вами, либо с ролью выше чем у Вас')

        member_warn = await self.db.get_warn(member = member)

        if member_warn is not None:
            return await ctx.error(description = 'У данного участника уже есть устный')
        
        error_fields = [
                    discord.EmbedField(
                     name = 'Пример, как правильно указывать время', 
                      value = '`2ч` — 2 часа\n`30мин` — 30 минут\n`1д` — 1 день'
                    ),
                    discord.EmbedField(
                        name = 'Доступные единицы измерения времени', 
                        value = '**секунда** — с, сек, секунд\n**минута** — м, мин, минут\n**час** — ч, часов\n**день** — д, дня, дней'
                    )
                ]

        warn_duration, warn_duration_type = get_duration(duration)

        if not(warn_duration.isdigit()):
            return await ctx.error(
                description = 'Вы указали не положительное число перед единицей времени',
                fields = error_fields
            )
        
        warn_duration = int(warn_duration)

        if warn_duration_type == 0:
            return await ctx.error(
                description = 'Вы указали неверный формат времени. Он должен начинаться с цифры, а заканчиваться единицей измерения времени.',
                fields = error_fields
            )

        elif warn_duration_type == 2:
            warn_duration *= 60
        elif warn_duration_type == 3:
            warn_duration *= 60 * 60
        elif warn_duration_type == 4:
            warn_duration *= 60 * 60 * 24
        
        warn_duration = datetime.timestamp(datetime.now()) + warn_duration
        max_duration = datetime.timestamp(datetime.now()) + 1209602 
                    
        if warn_duration > max_duration:
            return await ctx.error(description = 'Нельзя выдать устный длительностью больше 2 недель')
        
        await self.db.insert_warn(
            author = ctx.author,
            member = member,
            duration = int(warn_duration)
        )

            



def setup(bot):
    bot.add_cog(TempWarnsCog(bot))
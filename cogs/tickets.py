import discord
from utils import tickets_db, my_roles
from datetime import datetime
from discord.ext import commands

class OpenedTicketView(discord.ui.View):
    def __init__(self):
        self.db = tickets_db.TicketsDB()
        super().__init__(timeout = None)
    

    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_member:1001811269239722005>'), 
        style = discord.ButtonStyle.gray,
        custom_id = "ticket_claim",
        label = 'Принять тикет'
    )
    async def claim_callback(self, button, interaction):
        uroles = my_roles.Roles(interaction.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = interaction.user,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await interaction.response.send_message(f'Эта кнопка доступна только для следующих ролей:\n {roles_mention}', ephemeral = True)

        self.children[0].disabled = True
        await interaction.message.edit(view = self)
        await interaction.channel.set_permissions(interaction.user, send_messages=True, read_messages=True)

        ticket_overwrites = {}
        staff_roles = my_roles.Roles(interaction.guild).get_all_staff_roles()[:6]

        await self.db.claim_ticket(
            ticket_channel = interaction.channel,
            who_claimed = interaction.user
        )

        await interaction.response.send_message(f'{interaction.user.mention} (`{interaction.user}`) Будет обслуживать Ваш тикет')

        for i in staff_roles:
            await interaction.channel.set_permissions(i, send_messages = False)
            
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_tech:1001811218840952984>'), 
        style = discord.ButtonStyle.gray,
        custom_id = "ticket_close",
        label = 'Закрыть тикет'
    )
    async def close_callback(self, button, interaction):
        uroles = my_roles.Roles(interaction.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = interaction.user,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await interaction.response.send_message(f'Эта кнопка доступна только для следующих ролей:\n {roles_mention}', ephemeral = True)

        await self.db.delete_ticket(
            ticket_channel = interaction.channel,
            closed_by = interaction.user
        )    


class StartTicketView(discord.ui.View):
    def __init__(self):
        self.db = tickets_db.TicketsDB()
        self.mention_message = '<@&991219359731163187> <@&989892564691873793> <@&1009021230080348190> <@&989891381575159870>'
        super().__init__(timeout = None)
    
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_curator:1001817272240844911>'), 
        style = discord.ButtonStyle.green,
        custom_id = "open_ticket",
        label = 'Открыть тикет'
    )
    async def callback(self, button, interaction):
        async for i in self.db.cluster.tickets.tickets_list.find():
            if i["_id"] == 0:
                continue
            if i["author"] == interaction.user.id:
                return await interaction.response.send_message('Нельзя открыть более 1 тикета за раз', ephemeral = True)
        
        ticket_category = interaction.guild.get_channel(1004839366763495464)

        ticket_overwrites = {
            interaction.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            interaction.user: discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True),
        }

        staff_roles = my_roles.Roles(interaction.guild).get_all_staff_roles()[:6]

        if interaction.user.id != 1007615585506566205:
            for i in staff_roles:
                ticket_overwrites[i] = discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True)

        ticket_id = await self.db.insert_ticket(
            author = interaction.user,
            open_time = int(datetime.timestamp(datetime.now()))
        )

        ticket_channel = await ticket_category.create_text_channel(name = f'тикет-{ticket_id}', overwrites = ticket_overwrites)
        mention = await ticket_channel.send(self.mention_message)
        embticket = discord.Embed(
            title = f'Тикеты | Smesh',
            description = f'**──────── [<:asm_stormy_staff:1001811381554782280>] ────────**\n・Здравствуйте! Вы попали в свой тикет. Модерация поможет вам в кротчайшие сроки. Пока что можете написать цель создания тикета.',
            color = 0xbffed9
        )
        embticket.add_field(name = '**Примечания**', value = '・За попытки обмана администрации выдаётся предупреждение;\n\n・За бессмысленный тикет также выдаётся предупреждение\n**──────── [<:asm_stormy_staff:1001811381554782280>] ────────**', inline = False)
        await mention.delete() 
        await ticket_channel.send(f'{interaction.user.mention}', embed = embticket, view = OpenedTicketView())
        await interaction.response.send_message(f'Тикет успешно создан — {ticket_channel.mention}', ephemeral = True)
        
        



class TicketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = tickets_db.TicketsDB()

    slash_group = discord.SlashCommandGroup(name = 'ticket', guild_only = True, guild_ids = [837941760193724426])
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True )
    async def ticketstart(self, ctx):
        embticket = discord.Embed(
            title = 'Тикеты',
            description = 'Для открытия тикета используйте кнопку ниже',
            color = 0xbffed9
        )
        await ctx.message.delete()
        await ctx.send(embed = embticket, view = StartTicketView())
    
    @slash_group.command(name = 'close', description = 'Закрывает тикет')
    async def slash_ticket_close(self, ctx):
        uroles = my_roles.Roles(ctx.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = ctx.author,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await ctx.send_response(f'Эта команда доступна только для следующих ролей:\n {roles_mention}', ephemeral = True)

        if ctx.channel.category.id != 1004839366763495464 or ctx.channel.id == 1004832237872762980:
            return await ctx.send_response('Эта команда доступна только в категории тикетов', ephemeral  = True)

        await self.db.delete_ticket(
            ticket_channel = ctx.channel,
            closed_by = ctx.author
        )  

        await ctx.send_response('Тикет закрыт')
    
    @slash_group.command(name = 'claim', description = 'Принимает тикет')
    async def slash_ticket_claim(self, ctx):

        uroles = my_roles.Roles(ctx.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = ctx.author,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await ctx.send_response(f'Эта команда доступна только для следующих ролей:\n {roles_mention}', ephemeral = True)

        if ctx.channel.category.id != 1004839366763495464 or ctx.channel.id == 1004832237872762980:
            return await ctx.send_response('Эта команда доступна только в категории тикетов', ephemeral  = True)

        ticket_id = self.db.get_ticket_id(ctx.channel)
        db_ticket = await self.db.cluster["tickets"]["tickets_list"].find_one({"_id": ticket_id})

        if db_ticket["who_claimed"] != 0:
            return await ctx.send_response('Данный тикет уже и так принят', ephemeral  = True)

        async for message in ctx.channel.history(limit = 10, oldest_first = True):
            if message.author.id == self.bot.user.id:
                global first_message
                first_message = message
        
        ticket_view = discord.ui.View.from_message(first_message)
        ticket_view.children[0].disabled = True
        await first_message.edit(view = ticket_view)

        await ctx.channel.set_permissions(ctx.author, send_messages=True, read_messages=True)

        await self.db.claim_ticket(
            ticket_channel = ctx.channel,
            who_claimed = ctx.author
        )

        await ctx.channel.send(f'{ctx.author.mention} (`{ctx.author}`) Будет обслуживать Ваш тикет')

        ticket_overwrites = {}
        staff_roles = my_roles.Roles(ctx.guild).get_all_staff_roles()[:6]

        for i in staff_roles:
            await ctx.channel.set_permissions(i, send_messages = False)
        
        await ctx.send_response('Ок', ephemeral = True)



    @commands.command(aliases = ['с', 's', 'статистика'])
    @commands.guild_only()
    @commands.is_owner()
    async def tickets_stat(self, ctx, member: discord.Member = None):
        uroles = my_roles.Roles(ctx.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = ctx.author,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await ctx.error(description = f'Эта команда доступна только для следующих ролей:\n {roles_mention}')

        if member is None:
            member = ctx.author

        ticket_stat = self.db.get_claimed_data(member)

        embed = discord.Embed(
            title = 'Статистика'
        )
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(StartTicketView(), message_id = 1017472320048222250)
        self.bot.add_view(OpenedTicketView())
    

def setup(bot):
    bot.add_cog(TicketsCog(bot))
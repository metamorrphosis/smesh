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
        style = discord.ButtonStyle.green,
        custom_id = "claim_ticket",
        label = 'Закрыть тикет'
    )
    async def callback(self, button, interaction):
        uroles = my_roles.Roles(interaction.guild)
        staff_roles = uroles.get_all_staff_roles()
        check_roles = uroles.roles_check(
            member = interaction.user,
            roles_list = staff_roles
        )

        roles_mention = ', '.join(role.mention for role in staff_roles)

        if len(check_roles) == 0:
            return await interaction.response.send_message(f'Эта кнопка доступна только для следующих ролей:\n {roles_mention[2:]}', ephemeral = True)
    

    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_tech:1001811218840952984>'), 
        style = discord.ButtonStyle.green,
        custom_id = "close_ticket",
        label = 'Закрыть тикет'
    )
    async def callback(self, button, interaction):
        pass



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

        #for i in staff_roles:
            # ticket_overwrites[i] = discord.PermissionOverwrite(read_messages=True, send_messages=True, attach_files=True)

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
        await ticket_channel.send(embed = embticket, view = OpenedTicketView())
        await interaction.response.send_message(f'Тикет успешно создан — {ticket_channel.mention}', ephemeral = True)
        
        



class TicketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
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
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True )
    async def test(self, ctx):
        print(self.b)
        # await ctx.error(description = 'aa')
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(StartTicketView())
        self.bot.add_view(OpenedTicketView())
        print(OpenedTicketView().items)
    

def setup(bot):
    bot.add_cog(TicketsCog(bot))
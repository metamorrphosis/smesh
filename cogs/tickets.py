import discord
from utils import tickets_db, my_roles
from datetime import datetime
from discord.ext import commands

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
        await mention.delete()
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
    
    

def setup(bot):
    bot.add_cog(TicketsCog(bot))

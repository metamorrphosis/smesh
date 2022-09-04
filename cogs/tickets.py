import discord
from utils import database
from discord.ext import commands


class StartTicketView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
    
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_curator:1001817272240844911>'), 
        style = discord.ButtonStyle.green,
        custom_id = "open_ticket",
        label = 'Открыть тикет'
    )
    async def callback(self, button, interaction):
        pass


class TicketsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mention_message = '<@&991219359731163187> <@&989892564691873793> <@&1009021230080348190> <@&989891381575159870>'
    
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
        self.smesh_guild = self.bot.get_guild(837941760193724426)
        self.staff_role = self.smesh_guild.get_role(991219359731163187)
        self.helper_role = self.smesh_guild.get_role(989892564691873793)
        self.support_role = self.smesh_guild.get_role(1009021230080348190)
        self.moder_role = self.smesh_guild.get_role(989891381575159870)
        self.bot.add_view(StartTicketView())
    
    

def setup(bot):
    bot.add_cog(TicketsCog(bot))

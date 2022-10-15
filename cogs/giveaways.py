import discord
from discord import option
from utils import my_roles, giveaways_db
from datetime import datetime
from discord import option
from discord.ext import commands


class GiveawaysView(discord.ui.View):
    def __init__(self):
        self.db = giveaways_db.GiveawaysDB()
        super().__init__(timeout = None)
    
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str(''), 
        style = discord.ButtonStyle.green,
        custom_id = "aa",
        label = 'aa'
    )
    async def callback(self, button, interaction):
        pass


class GiveawaysCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.db = giveaways_db.GiveawaysDB()    
    
    @commands.slash_command(
        guild_ids = [837941760193724426],
        name = 'giveaway', 
        description = 'Создаёт новый розыгрыш (доступно только администрации)'
    )
    @discord.default_permissions(administrator = True)
    
    @option(
        name = 'Канал',
        description = 'Канал, в котором происходит розыгрыш',
        input_type = discord.TextChannel,
        required = True
    )
    @option(
        name = 'Айди сообщения',
        description = 'Айди сообщения с вебхуком розыгрыша',
        input_type = int,
        required = True
    )
    @option(
        name = 'Время',
        description = 'Время, через которое закончится розыгрыш',
        input_type = str,
        required = True
    )
    @option(
        name = 'Приз',
        description = 'Приз розыгрыша',
        input_type = str,
        required = True
    )
    async def slash_new_giveaway(self, ctx, 
        channel: discord.TextChannel, 
        message_id: int, 
        end_time: str, 
        prize: str
    ):
        await ctx.send_response(f'{channel} {message_id} {end_time} {prize}', ephemeral = True)

    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(GiveawaysView())
    

def setup(bot):
    bot.add_cog(GiveawaysCog(bot))

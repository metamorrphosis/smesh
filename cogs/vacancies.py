import discord
import asyncio
from discord.ext import commands
from datetime import datetime, timezone


class HelperModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Сколько Вам лет? Как называть?",
                placeholder="Пример: 15 лет, Петя",
                min_length=4,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Сколько времени Вы сможете уделять серверу?",
                placeholder="Пример: 5 часов в день, от 17:00 до 22:00",
                min_length=1,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Как Вы относитесь к текущей администрации?",
                placeholder="Пример: Пока что хорошее впечатление, надеюсь оно не изменится",
                min_length=4,
                max_length=150,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Раскажите про себя, чем вы лучше других?",
                placeholder="Пример: Я лучше других, потому что — я умею мыслить критически, я креативный, не агрессивный",
                min_length= 20,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Ваш опыт в модерации на других серверах",
                placeholder="Пример: Был старшим модератором на сервере Death gun'а 3 месяца",
                min_length=2,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            *args,
            **kwargs,
        )

    async def callback(self, interaction):
        timereg = int(interaction.user.created_at.replace(tzinfo=timezone.utc).timestamp())
        timejoin = int(interaction.user.joined_at.replace(tzinfo=timezone.utc).timestamp())

        embed = discord.Embed(
            title="Новая анкета на помощника в дискорде",
            fields=[
                discord.EmbedField(
                    name = "Автор анкеты", 
                    value = f"{interaction.user.mention} | {interaction.user} | {interaction.user.id}", 
                    inline = False
                ),
                discord.EmbedField(
                    name = "Информация по автору анкеты", 
                    value = f'Дата регистрации аккаунта: <t:{timereg}>\nДата присоединения на сервер: <t:{timejoin}>', 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[0].label, 
                    value = self.children[0].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[1].label, 
                    value = self.children[1].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[2].label, 
                    value = self.children[2].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[3].label, 
                    value = self.children[3].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[4].label, 
                    value = self.children[4].value, 
                    inline = False
                ),
            ],
            color = 0x2e3133,
            timestamp = datetime.now()
        )
        channel = interaction.guild.get_channel(1007118729697562715)
        await channel.send(embed = embed)
        await interaction.response.send_message('Ваша заявка успешно отправлена администрации', ephemeral = True)


class TelegramModal(discord.ui.Modal):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            discord.ui.InputText(
                label="Ваше имя",
                placeholder="Пример: Петя",
                min_length=1,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Ваш часовой пояс",
                placeholder="Пример: МСК",
                min_length=1,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Ваш телеграмм",
                placeholder="Пример: @petya228",
                min_length=2,
                max_length=100,
                style=discord.InputTextStyle.short,
                required=True,
            ),
            discord.ui.InputText(
                label="Был ли у Вас опыт в подобной сфере?",
                placeholder="Пример: Да был, в телеграмм канале (23,000 участников)",
                min_length= 2,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Сколько времени Вы сможете уделять телеграмму",
                placeholder="Пример: Два-три часа в день",
                min_length=2,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            *args,
            **kwargs,
        )

    async def callback(self, interaction):
        timereg = int(interaction.user.created_at.replace(tzinfo=timezone.utc).timestamp())
        timejoin = int(interaction.user.joined_at.replace(tzinfo=timezone.utc).timestamp())

        embed = discord.Embed(
            title="Новая анкета на модератора телеграмм",
            fields=[
                discord.EmbedField(
                    name = "Автор анкеты", 
                    value = f"{interaction.user.mention} | {interaction.user} | {interaction.user.id}", 
                    inline = False
                ),
                discord.EmbedField(
                    name = "Информация по автору анкеты", 
                    value = f'Дата регистрации аккаунта: <t:{timereg}>\nДата присоединения на сервер: <t:{timejoin}>', 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[0].label, 
                    value = self.children[0].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[1].label, 
                    value = self.children[1].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[2].label, 
                    value = self.children[2].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[3].label, 
                    value = self.children[3].value, 
                    inline = False
                ),
                discord.EmbedField(
                    name = self.children[4].label, 
                    value = self.children[4].value, 
                    inline = False
                ),
            ],
            color = 0x2e3133,
            timestamp = datetime.now()
        )
        channel = interaction.guild.get_channel(1007118729697562715)
        await channel.send(embed = embed)
        await interaction.response.send_message('Ваша заявка успешно отправлена администрации', ephemeral = True)


class HelperView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_helper:1018512420282564628>'), 
        label = 'Заявка на помощника в дискорде', 
        style = discord.ButtonStyle.gray, 
        custom_id = "helper_modal"
    )
    async def helper(self, button, interaction):
        await interaction.response.send_modal(HelperModal(title = 'Заявка на роль помощника в дискорд'))


class TelegramView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_telegram:1020336781650042942>'), 
        label = 'Заявка на модератора телеграмм', 
        style = discord.ButtonStyle.gray, 
        custom_id = "telegram_modal"
    )
    async def helper(self, button, interaction):
        await interaction.response.send_modal(TelegramModal(title = 'Заявка на роль модератора в телеграмм'))


class VacanciesCog(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
        self.hook_url = 'https://discord.com/api/webhooks/1018488382059462726/1X5vAr1FqtsgqNs2KgKUTDKeTS46_99CVapek6R_yyHeerwYU8U_cHf8tveRqrWm2Fzi'
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True )
    async def vcs(self, ctx):
        embhelper = [
            discord.Embed(
                color = 0xbffed9
            ),
            discord.Embed(
                title = '<:asm_list:1018821075926253568>・Набор на роль Помощника в дискорд',
                description = '━────────────────━\n**Требования для подачи заявки:**\n<:asm_green_dot:1018821297481994280>Не менее 14 полных лет.\n<:asm_white_dot:1018821114853601353>Знание правил сервера.\n<:asm_green_dot:1018821297481994280>10 уровень в JuniperBot.\n<:asm_white_dot:1018821114853601353>Опыт работы в подобной сфере.\n\n**Что мы можем предложить взамен:**\n<:asm_green_dot:1018821297481994280>Зарплата игровой валютой в виде <:vajno_2:1018512718585679882>.',
                color = 0xbffed9
            )
        ]
        embtg = [
            discord.Embed(
                title = '<:asm_list:1018821075926253568>・Набор на роль Модератора в телеграмм',
                description = '━────────────────━\n**Требования для подачи заявки:**\n<:asm_green_dot:1018821297481994280>Не менее 14 полных лет.\n<:asm_white_dot:1018821114853601353>Знание правил в телеграмм группе.\n<:asm_green_dot:1018821297481994280>Активное появление в телеграмме.\n\n**Что мы можем предложить взамен:**\n<:asm_white_dot:1018821114853601353>Опыт работы в подобной сфере.\n<:asm_green_dot:1018821297481994280>Новые знакомства и коллектив.',
                color = 0xbffed9
            )
        ]
        
        embhelper[0].set_image(url = 'https://media.discordapp.net/attachments/1017458641537859604/1018507896327249961/1662901405981.png')
        embhelper[1].set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')
        embtg[0].set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')
        
        await ctx.message.delete()
        channel = ctx.guild.get_channel(1005221671432618045)
        webhook = await channel.webhooks()
        webhook = webhook[0]

        await webhook.send(embeds = embhelper, view = HelperView())
        await asyncio.sleep(4)
        await webhook.send(embeds = embtg, view = TelegramView())
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True )
    async def hookk(self, ctx):
        chan = ctx.guild.get_channel(1004655452044398622)
        hk = await chan.create_webhook(name = 'Smesh')
        await ctx.message.reply(hk)
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(HelperView())
        self.bot.add_view(TelegramView())


def setup(bot):
    bot.add_cog(VacanciesCog(bot))

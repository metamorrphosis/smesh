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
        channel = interaction.guild.get_channel(config.vacancies_answers_channel)
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
        channel = interaction.guild.get_channel(config.vacancies_answers_channel)
        await channel.send(embed = embed)
        await interaction.response.send_message('Ваша заявка успешно отправлена администрации', ephemeral = True)



class EventerModal(discord.ui.Modal):
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
                label="Был ли у Вас опыт в подобной сфере",
                placeholder="Пример: Да был, на сервере Shampanov",
                min_length= 2,
                max_length=500,
                style=discord.InputTextStyle.long,
                required=True,
            ),
            discord.ui.InputText(
                label="Сколько времени Вы сможете уделять ивентам",
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
            title="Новая анкета на ивент мейкера",
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
                )
            ],
            color = 0x2e3133,
            timestamp = datetime.now()
        )
        channel = interaction.guild.get_channel(config.vacancies_answers_channel)
        await channel.send(embed = embed)
        await interaction.response.send_message('Ваша заявка успешно отправлена администрации', ephemeral = True)


class VacancyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_helper:1018512420282564628>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "helper_modal"
    )
    async def helper(self, button, interaction):
        await interaction.response.send_modal(HelperModal(title = 'Заявка на роль помощника в дискорд'))
    
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_party:1018512458538815528>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "eventer_modal"
    )
    async def eventer(self, button, interaction):
        await interaction.response.send_modal(EventerModal(title = 'Заявка на роль ивент мейкера'))

    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:a_telegram:1020336781650042942>'), 
        style = discord.ButtonStyle.gray, 
        custom_id = "telegram_modal"
    )
    async def telegram(self, button, interaction):
        await interaction.response.send_modal(TelegramModal(title = 'Заявка на роль модератора в телеграмм'))

class VacanciesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True )
    async def vcs(self, ctx):
        embeds = [
            discord.Embed(
                color = 0xbffed9
            ),
            discord.Embed(
                title = 'Набор в персонал сервера',
                description = '''<:e_white_dot:1018821114853601353>Чтобы подать свою заявку и стать частью персонала, просто нажмите на кнопку ниже. С интересующей вас должностью!

<:a_helper:1018512420282564628> - подать заявку на помощника
<:a_party:1018512458538815528> - подать заявку на ивент мейкера
<:a_telegram:1020336781650042942> - подать заявку на модератора в телеграмм''',
                color = 0xbffed9
            )
        ]
        
        embeds[1].set_image(url = 'https://cdn.discordapp.com/attachments/1017458641537859604/1018492145335816192/SAVE_20220710_205848.jpg')
        embeds[0].set_image(url = 'https://media.discordapp.net/attachments/1006991678994919464/1032339098985300140/20221019_003819.png?width=1440&height=432')
        
        await ctx.message.delete()
        channel = ctx.guild.get_channel(config.vacancies_channel)
        webhook = await channel.webhooks()
        webhook = webhook[0]

        await webhook.send(embeds = embeds, view = VacancyView())
    

        
    
    @commands.Cog.listener()
    async def on_ready(self):
        self.bot.add_view(VacancyView())



def setup(bot):
    bot.add_cog(VacanciesCog(bot))

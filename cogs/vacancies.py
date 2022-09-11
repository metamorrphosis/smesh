import discord
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
            title="Новая анкета на помощника ",
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


class VacancyView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout = None)
     
    @discord.ui.button(
        emoji = discord.PartialEmoji.from_str('<:asm_stormy_curator:1001817272240844911>'), 
        label = 'Заявка на помощника', 
        style = discord.ButtonStyle.gray, 
        custom_id = "helper_modal"
    )
    async def helper(self, button, interaction):
        await interaction.response.send_modal(HelperModal(title = 'Заявка на помощника'))

class Vacancies(commands.Cog):    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.guild_only()
    @commands.has_guild_permissions( administrator = True)
    async def vcs(self, ctx):
        embvcs = discord.Embed(
            title = 'Требования для подачи заявки на роль Помощника',
            description = '──────── [ <:asm_storm_admin:1001811084333830174> ] ────────\n**Наши требования:**\n> <:asm_stormy_5:1001811300399185940>Не менее 14 полных лет\n> <:asm_stormy_5:1001811300399185940>Знание правил сервера\n> <:asm_stormy_5:1001811300399185940>Находится на сервере не менее 2-ух недель\n> <:asm_stormy_5:1001811300399185940>Минимум 5 уровень в `JuniperBot`\n──────── [ <:asm_storm_admin:1001811084333830174> ] ────────\n**Что мы можем предложить взамен:**\n> <:asm_stormy_5:1001811300399185940>Игровая валюта <:vajno_2:996395333322023032>\n\nДля подачи заявки используйте кнопку ниже',
            color = 0x2e3133
        )
        await ctx.message.delete()
        await ctx.send(embed = embvcs, view = VacancyView())


def setup(bot):
    bot.add_cog(Vacancies(bot))

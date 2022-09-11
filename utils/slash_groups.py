import discord
from discord.ext import commands

tickets_group = commands.SlashCommandGroup(
    name = 'ticket', 
    description = 'Взаимодействие с тикетами', 
    guild_ids = [837941760193724426], 
    guild_only = True
)
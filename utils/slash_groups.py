import discord
from discord.ext import commands
from discord.commands import SlashCommandGroup

tickets_group = SlashCommandGroup(
    name = 'ticket', 
    description = 'Взаимодействие с тикетами', 
    guild_ids = [837941760193724426], 
    guild_only = True
)
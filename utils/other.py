import discord
from datetime import datetime, timedelta

def nc(arg: str) -> str:
    step, new_str = 0, ''

    for i in arg[::-1]:
        if step == 3:
            new_str += ','
            step = 0

        new_str += i
        step += 1
    
    return new_str[::-1]


def get_duration(number: str) -> str:
    if number.endswith('с'):
        return number[:-1], 1
    elif number.endswith('сек'):
        return number[:-3], 1
    elif number.endswith('секунд'):
        return number[:-6], 1
    elif number.endswith('м'):
        return number[:-1], 2
    elif number.endswith('мин'):
        return number[:-3], 2
    elif number.endswith('минут'):
        return number[:-5], 2
    elif number.endswith('ч'):
        return number[:-1], 3
    elif number.endswith('часов'):
        return number[:-5], 3
    elif number.endswith('д'):
        return number[:-1], 4
    elif number.endswith('дней'):
        return number[:-4], 4
    elif number.endswith('дня'):
        return number[:-3], 4
    else:
        return '1', 0


async def auto_role(member: discord.Member, role: discord.Role) -> str:
    if role in member.roles:
        await member.remove_roles(role)
        return f'Успешно снял у вас роль {role.mention}'
    else:
        await member.add_roles(role)
        return f'Успешно выдал вам роль {role.mention}'
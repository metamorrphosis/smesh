import discord

def nc(arg: str) -> str:
    step, new_str = 0, ''

    for i in arg[::-1]:
        if step == 3:
            new_str += ','
            step = 0

        new_str += i
        step += 1
    
    return new_str[::-1]


async def auto_role(member: discord.Member, role: discord.Role) -> str:
    if role in member.roles:
        await member.remove_roles(role)
        return f'Успешно снял у вас роль {role.mention}'
    else:
        await member.add_roles(role)
        return f'Успешно выдал вам роль {role.mention}'
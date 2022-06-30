import discord
import asyncio


async def mute(ctx, member : discord.Member, time : int):
    emb = discord.Embed(colour=discord.Color.red())
    mute_role = discord.utils.get(ctx.message.guild.roles, name= 'MUTE')
    
    await member.add_roles(mute_role)

    emb.add_field(name=f'Игроку {member.name} выдано ограничение чата!', value=f'На {time} секунд')
    emb.set_footer(text=f'Администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

    await asyncio.sleep(time)
    emb = discord.Embed(colour=discord.Color.green())
    emb.add_field(name=f'Игроку {member.name} возращен доступ  к чату!', value=f'он был отстранен на {time} секунд')
    
    await ctx.send(embed=emb)

    await member.remove_roles(mute_role)
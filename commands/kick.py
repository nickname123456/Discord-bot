import discord

async def kick(ctx, member: discord.Member, reason):
    emb = discord.Embed(colour=discord.Color.red())

    await member.kick(reason=reason)

    emb.add_field(name=f'Игрок {member.name} удален!', value=f'Причина: {reason}')
    emb.set_footer(text=f'администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)
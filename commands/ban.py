import discord

async def ban(ctx, member: discord.Member, reason):
    emb = discord.Embed(colour=discord.Color.red())

    await member.ban(reason = reason)

    emb.add_field(name=f'Игрок {member.name} ЗАБАНЕН с концами!', value=f'Причина: {reason}')
    emb.set_footer(text=f'Администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)

async def unban(ctx, member: discord.Member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user
        mention = ban_entry.user.mention
        if mention == member:
            await ctx.guild.unban(user)

            emb = discord.Embed(colour=discord.Color.red())
            emb.add_field(name=f'Игрок {user.name} РАЗБАНЕН!', value='Не знаю почему, видимо админ простил')
            emb.set_footer(text=f'Администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)
            await ctx.send(embed=emb)
            return
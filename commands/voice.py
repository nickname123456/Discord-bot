import discord

voice = None

async def voice(ctx, voice_clients):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await ctx.send(f'Я присоеденился к каналу {channel}')


async def leave(ctx, voice_clients):
    channel = ctx.message.author.voice.channel
    voice = discord.utils.get(voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        await ctx.send(f'Я отключился от канала {channel}')
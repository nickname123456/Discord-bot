import imp
import discord
from settings import PREFIX

async def help(ctx):
    emb = discord.Embed(title='Навигация по боту')

    emb.add_field( name=f'{PREFIX}переверни [текст]', value='переворачивает ваш текст' )
    emb.add_field( name=f'{PREFIX}пикча', value='показывает случайную картинку' )
    emb.add_field( name=f'{PREFIX}удали [кол-во сообщений]', value='чистит чат' )
    emb.add_field( name=f'{PREFIX}кик [упоминание участника]', value='удаляет человека с сервера' )
    emb.add_field( name=f'{PREFIX}бан [упоминание участника]', value='блокирует доступ к серверу' )
    emb.add_field(name=f'{PREFIX}разбан [имя и тэг]', value='разблокирует доступ к серверу')

    await ctx.send(embed = emb)
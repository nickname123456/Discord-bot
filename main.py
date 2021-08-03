from sys import prefix
import discord
from discord import colour
from discord.embeds import Embed
from discord.ext import commands
import os
import requests
import random
import datetime

REPLACEMENT_MAP = {
    "a": "ɐ",
    "b": "q",
    "c": "ɔ",
    "d": "p",
    "e": "ǝ",
    "f": "ɟ",
    "g": "ƃ",
    "h": "ɥ",
    "i": "ᴉ",
    "j": "ɾ",
    "k": "ʞ",
    "l": "l",
    "m": "ɯ",
    "n": "u",
    "o": "o",
    "p": "d",
    "q": "b",
    "r": "ɹ",
    "s": "s",
    "t": "ʇ",
    "u": "n",
    "v": "ʌ",
    "w": "ʍ",
    "x": "x",
    "y": "ʎ",
    "z": "z",
    "A": "∀",
    "B": "B",
    "C": "Ɔ",
    "D": "D",
    "E": "Ǝ",
    "F": "Ⅎ",
    "G": "פ",
    "H": "H",
    "I": "I",
    "J": "ſ",
    "K": "K",
    "L": "˥",
    "M": "W",
    "N": "N",
    "O": "O",
    "P": "Ԁ",
    "Q": "Q",
    "R": "R",
    "S": "S",
    "T": "┴",
    "U": "∩",
    "V": "Λ",
    "W": "M",
    "X": "X",
    "Y": "⅄",
    "Z": "Z",
    "0": "0",
    "1": "Ɩ",
    "2": "ᄅ",
    "3": "Ɛ",
    "4": "ㄣ",
    "5": "ϛ",
    "6": "9",
    "7": "ㄥ",
    "8": "8",
    "9": "6",
    ",": "'",
    ".": "˙",
    "?": "¿",
    "!": "¡",
    '"': ",,",
    "'": ",",
    "(": ")",
    ")": "(",
    "[": "]",
    "]": "[",
    "{": "}",
    "}": "{",
    "<": ">",
    ">": "<",
    "&": "⅋",
    "_": "‾",
    'й': 'ņ',
    'ц': 'ǹ',
    'у': 'ʎ',
    'к': 'ʞ',
    'е': 'ǝ',
    'н': 'н',
    'г': 'ɹ',
    'ш': 'm',
    'щ': 'm',
    'з': 'ε',
    'х': 'х',
    'ъ': 'q',
    'ф': 'ф',
    'ы': 'ıq',
    'в': 'ʚ',
    'а': 'ɐ',
    'п': 'u',
    'р': 'd',
    'о': 'о',
    'л': 'v',
    'д': 'ɓ',
    'ж': 'ж',
    'э': 'є',
    'я': 'ʁ',
    'ч': 'һ',
    'с': 'ɔ',
    'м': 'w',
    'и': 'и',
    'т': 'ɯ',
    'ь': 'q',
    'б': 'ƍ',
    'ю': 'oı'
}

PREFIX = '!'
client = commands.Bot(PREFIX)
client.remove_command('help')






@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

'''
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    msg = message.content.lower()

    if msg == '!бот':
        await message.channel.send('Слит(')
    
    if msg.startswith('!удали '):
        print(msg[7:])
        await message.channel.purge(limit = msg[7:])

    if msg.startswith('!переверни '):
        text = message.content[11:]
        final_str = ""
        for char in text:
            if char in REPLACEMENT_MAP.keys():
                new_char = REPLACEMENT_MAP[char]
            else:
                new_char = char
            final_str += new_char
        if text != final_str:
            await message.channel.send(final_str)
        else:
            await message.channel.send(text)

    if msg == '!пикча':
        await message.channel.send("http://lorempixel.com/" + str(random.randint(100, 1000)) +  "/" + str(random.randint(100, 1000)) + "/")
'''

@client.command()

async def бот(ctx):
    await ctx.send('Слит(')



@client.command()

async def переверни(ctx, text):
    final_str = ""
    for char in text:
        if char in REPLACEMENT_MAP.keys():
            new_char = REPLACEMENT_MAP[char]
        else:
            new_char = char
        final_str += new_char
    if text != final_str:
        await ctx.send(final_str)
    else:
        await ctx.send(text)



@client.command()

async def пикча(ctx):
    await ctx.send("http://lorempixel.com/" + str(random.randint(100, 1000)) + "/" + str(random.randint(100, 1000)) + "/")



@client.command()
@commands.has_permissions(administrator = True)

async def удали(ctx, amount = 10):
    try:
        await ctx.channel.purge(limit = amount)
    except discord.ext.commands.errors.MissingPermissions:
        await ctx.send('Недостаточно прав!')



@client.command()
@commands.has_permissions(administrator=True)

async def кик(ctx, member: discord.Member, *, reason = 'просто так'):
    emb = discord.Embed(colour=discord.Color.red())

    await member.kick(reason=reason)

    emb.add_field(name=f'Игрок {member.name} удален!',
                  value=f'Причина: {reason}')
    emb.set_footer(
        text=f'администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)



@client.command()
@commands.has_permissions(administrator=True)

async def бан(ctx, member: discord.Member, *, reason='просто так'):
    emb = discord.Embed(colour=discord.Color.red())

    await member.ban(reason = reason)

    emb.add_field(name=f'Игрок {member.name} заблокирован!',
                  value=f'Причина: {reason}')
    emb.set_footer(
        text=f'администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)



@client.command()
@commands.has_permissions(administrator=True)

async def разбан(ctx, *, member):
    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user
        if str(user) == str(member):
            await ctx.guild.unban(user)
            await ctx.send(f'{user.mention} разблокирован!')
            return



@client.command()
async def помощь(ctx):
    emb = discord.Embed(title='Навигация')

    emb.add_field( name=f'{PREFIX}переверни [текст]', value='переворачивает ваш текст' )
    emb.add_field( name=f'{PREFIX}пикча', value='показывает случайную картинку' )
    emb.add_field( name=f'{PREFIX}удали [кол-во сообщений]', value='чистит чат' )
    emb.add_field( name=f'{PREFIX}кик [упоминание участника]', value='удаляет человека с сервера' )
    emb.add_field( name=f'{PREFIX}бан [упоминание участника]', value='блокирует доступ к серверу' )
    emb.add_field(name=f'{PREFIX}разбан [имя и тэг]', value='разблокирует доступ к серверу')

    await ctx.send(embed = emb)


@client.command()
async def тест(ctx):
    emb = discord.Embed(title='Тайтл', description = 'description' , colour = discord.Color.dark_magenta(), url = 'https://d2xzmw6cctk25h.cloudfront.net/post/2236/og_image/39ed77ccb6aab5ebc24f4f59a94f1674.png')
    emb.set_author(name= client.user.name, icon_url= client.user.avatar_url)
    emb.set_footer(text = ctx.author.name, icon_url= ctx.author.avatar_url)
    emb.set_image(url = 'https://media.istockphoto.com/photos/clock-face-9-oclock-picture-id489971205')
    emb.set_thumbnail(url = 'https://play-lh.googleusercontent.com/Wvjx6rVlC1rGWKkln3r-23ICKV--sxEEUuq7jd15BeJan8v-wS7TGwm0NHXqqon18w')
    
    now_date = datetime.datetime.now()
    emb.add_field(name=now_date, value='текущее время')

    await ctx.send(embed = emb)


@client.command()
@commands.has_permissions(administrator=True)

async def мут(ctx, member : discord.Member, reason = 'по рофлу'):
    emb = discord.Embed(colour=discord.Color.red())
    mute_role = discord.utils.get(ctx.message.guild.roles, name= 'MUTE')
    
    await member.add_roles(mute_role)

    emb.add_field(name=f'Игроку {member.name} выдано ограничение чата!',
                  value=f'Причина: {reason}')
    emb.set_footer(
        text=f'администратор {ctx.author.name}', icon_url=ctx.author.avatar_url)

    await ctx.send(embed=emb)






client.run("ODcwOTY1NTk1NTY5NTQxMTIw.YQUb6w.pGjHuonNiAgJgZfBWUx3NQH7YXI")

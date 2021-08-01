import discord
from discord.ext import commands
import os
import requests
import random

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


client = commands.Bot(command_prefix= "!")






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
    await member.kick(reason = reason)
    await ctx.send(str(member) + 'удален!')




client.run("ODcwOTY1NTk1NTY5NTQxMTIw.YQUb6w.4yj1or4VS0clKq_ovI0NW7eYadA")

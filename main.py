import discord
from discord.utils import get
from discord.ext import commands
import random
import datetime
import asyncio
from commands.voice import leave, voice

from settings import REPLACEMENT_MAP, PREFIX, id_noob_role, id_channel_threshold
from commands.turn_over import turn_over
from commands.random_picture import random_picture
from commands.kick import kick
from commands.ban import ban, unban
from commands.help import help
from commands.mute import mute


playground = ['1', '2', '3',
              '4', '5', '6',
              '7', '8', '9']

free = playground.copy()
place = ''
tic = 'x'
tac = 'o'
waiting_game = False
who_ttt_wait = ''
ttt_wait = False
gameMember_list = {1: '', 
                   2: ''}
game_is_on = False




client = commands.Bot(PREFIX, intents = discord.Intents.all())
client.remove_command('help')






@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online, activity = discord.Game("Че смотришь?"))
    print('We have logged in as {0.user}'.format(client))




@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f'{ctx.author.mention}, ты слишком мал для владения этой командой!')
    
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'{ctx.author.mention}, ты забыл написать аргумент команды)')
    
    elif isinstance(error, commands.CommandNotFound):
        await ctx.send(f'{ctx.author.mention}, сорян, но такую команду еще не завезли(((')
    
    elif isinstance(error, commands.MemberNotFound):
        await ctx.send(f'{ctx.author.mention}, такого чела нет на нашем сервере!')
    
    else:
        await ctx.send(f'@StrangeSturgeon, тут неожиданная ошибка: {error}')



@client.event
async def on_member_join(member):
    channel = client.get_channel(id_channel_threshold)
    role = discord.utils.get(member.guild.roles, id=id_noob_role)

    await member.add_roles(role)
    await channel.send(embed = discord.Embed(description = f'Пользователь ``{member.name}`` залетел к нам!', color = 0xDE2A5A))
    



@client.event
async def on_reaction_add(reaction, user):
    print(1)
    Channel = client.get_channel(871021488197738496)
    print(2)
    if reaction.message.channel.id != Channel:
        print(3)
        return
    if reaction.emoji == ":heart:":
        print(4)
        Role = discord.utils.get(user.server.roles, id=872089259920724060)
        print(5)
        await client.add_roles(user, Role)
        print(6)
    
    if reaction.emoji == ":clown:":
        print(7)
        Role = discord.utils.get(user.server.roles, id=872088568787529728)
        print(8)
        await client.add_roles(user, Role)
        print(9)




@client.command()
async def бот(ctx):
    await ctx.send('Слит(')



@client.command()
async def переверни(ctx, *, text):
    await turn_over(ctx, text)



@client.command()
async def пикча(ctx):
    await random_picture(ctx)



@client.command()
@commands.has_permissions(administrator = True)
async def удали(ctx, amount = 10):
    if amount <= 100:
        await ctx.channel.purge(limit = amount)
    else:
        await ctx.send('Не, ну я тебе не дам столько удалить! палехче будь пэжэ')



@client.command()
@commands.has_permissions(administrator=True)
async def кик(ctx, member: discord.Member, *, reason = 'по рофлу'):
    await kick(ctx, member, reason)



@client.command()
@commands.has_permissions(administrator=True)
async def бан(ctx, member: discord.Member, *, reason='по рофлу'):
    await ban(ctx, member, reason)



@client.command()
@commands.has_permissions(administrator=True)
async def разбан(ctx, *, member):
    await unban(ctx, member)




@client.command()
async def помощь(ctx):
    await help(ctx)


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
async def мут(ctx, member : discord.Member, time : int):
    await mute(ctx, member, time)





@client.command()
async def передай(ctx, member: discord.Member, *, message):
    await member.send(f'{member.name}, привет! {ctx.author.name} просил передать "{message}"')
    await ctx.send('Я передал!')





@client.command()
async def ттт(ctx):
    global gameMember_list
    global waiting_game

    waiting_game = True
    for i in ctx.author.mention:
        gameMember_list[1] += i
    await ctx.send('Начался набор в игру крестики-нолики! \nДля входа напиши "!зайти"')



@client.command()
async def зайти(ctx):
    global gameMember_list
    global waiting_game
    global game_is_on

    if waiting_game == True:
        for i in ctx.author.mention:
            gameMember_list[2] += i
        waiting_game == False
        await ctx.send(f'Началась игра крестики нолики. \n:x: - {gameMember_list[1]}\n:o: - {gameMember_list[2]}')
        game_is_on = True

        await ttt(ctx)
    else:
        await ctx.send('Сейчас не ведется набор в игру. \nЧтобы начать набор пиши "!ттт"')





async def output():
    global place
    place = ''
    num = 0
    for i in playground:
        if num != 3:
            place += f'|{i}'
            num += 1
        else:

            place += f'\n'
            place += f'-------'
            place += f'\n|{i}'
            num = 1
    return place


async def replacement(was, became):
    was_index = playground.index(was)

    playground.remove(was)
    free.remove(was)
    playground.insert(was_index, became)


async def opponents_move():
    if len(free) > 0:
        return random.choice(free)


async def check_win():
    win_coord = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                 (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_coord:
        if playground[each[0]] == playground[each[1]] == playground[each[2]]:
            return playground[each[0]]
    return False




async def ttt(ctx):
    global ttt_wait, tic, who_ttt_wait, free, place, tac, waiting_game, gameMember_list, game_is_on
    while await check_win() == False and len(free) != 0:
        await asyncio.sleep(1)
        while ttt_wait == False and await check_win() == False:
            await ctx.send(f'Выберай\n {await output()}')
            if who_ttt_wait != gameMember_list[1]:
                who_ttt_wait = gameMember_list[1]
                ttt_wait = True

            else:
                if await check_win() == False and ttt_wait == False:
                    who_ttt_wait = gameMember_list[2]
                    ttt_wait = True
    global playground
    if await check_win() == False and len(free) == 0:

        playground = ['1', '2', '3',
                      '4', '5', '6',
                      '7', '8', '9']

        free = playground.copy()
        place = ''
        tic = 'x'
        tac = 'o'
        waiting_game = False
        who_ttt_wait = ''
        ttt_wait = False
        gameMember_list = {1: '',
                        2: ''}
        game_is_on = False

        await ctx.send('Ничья')
        return

    

    free = playground.copy()
    place = ''
    tic = 'x'
    tac = 'o'
    waiting_game = False
    who_ttt_wait = ''
    ttt_wait = False
    gameMember_list = {1: '',
                       2: ''}
    game_is_on = False

    await ctx.send(f'Выйграл :{await check_win()}:')


@client.command()
async def ход(ctx, num):
    global ttt_wait
    if not game_is_on:
        await ctx.send(f'{ctx.author.mention}, сейчас не идет игра')
        return
    
    author = ''
    for i in ctx.author.mention:
        author += i
    if author != who_ttt_wait:
        await ctx.send(f'{author}, сейчас не ты ходишь!')
        return

    if num not in free:
        await ctx.send(f'{author}, эта клетка занята!')
        return
    
    if gameMember_list[1] == who_ttt_wait:
        await replacement(num, tic)
        ttt_wait = False
        
    elif gameMember_list[2] == who_ttt_wait:
        await replacement(num, tac)
        ttt_wait = False




@client.command()
@commands.has_permissions(administrator=True)
async def Ягуль(ctx):
    ghoul = 1000
    while ghoul >= 6:
        await ctx.send(f'{ghoul}-7={ghoul-7}')
        ghoul -= 7



@client.command()
@commands.has_permissions(administrator=True)
async def войс(ctx):
    await voice(ctx, client.voice_clients)


@client.command()
@commands.has_permissions(administrator=True)
async def ливни(ctx):
    await leave(ctx, client.voice_clients)


client.run("ODcwOTY1NTk1NTY5NTQxMTIw.YQUb6w.78Rw9yblmQ1o_WXyWd2TKTyfWaw")

from random import randint

async def random_picture(ctx):
    num1 = randint(100, 4000)
    num2 = randint(100, 4000)
    random_choise = randint(0, 7)

    if random_choise == 0: pic = f"https://loremflickr.com/{num1}/{num2}"
    elif random_choise == 1: pic = f"https://placekitten.com/{num1}/{num2}"
    elif random_choise == 2: pic = f"https://baconmockup.com/{num1}/{num2}"
    elif random_choise == 3: pic = f"https://placebeard.it/{num1}x{num2}"
    elif random_choise == 4: pic = f"http://placeimg.com/{num1}/{num2}/any"
    elif random_choise == 5: pic = f"https://placebear.com/{num1}/{num2}"
    elif random_choise == 6: pic = f"https://www.stevensegallery.com/{num1}/{num2}"
    else: pic = f"https://picsum.photos/{num1}/{num2}"

    await ctx.send(pic)
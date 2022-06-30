from settings import REPLACEMENT_MAP

async def turn_over(ctx, text):
    text = text[len(text)::-1]
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
import discord
import random
from botfunc import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh: int = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def password(ctx, total: int = 5):
    await ctx.send(gen_pass(total))


@bot.command()
async def guessing(ctx):
    global number
    number = random.randint(1, 20)
    await ctx.send("Pick a number from 1 to 20.")

@bot.command()
async def answer(ctx, ans):
    if number == int(ans):
        await ctx.send("Correct.")
    else:
        await ctx.send("Wrong. Retry?")

bot.run("")

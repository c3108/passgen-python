import discord
import random
from botfunc import gen_pass
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

# Active number games per user
active_numbers = {}

# Scoreboard per user
user_scores = {}

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
    number = random.randint(1, 20)
    active_numbers[ctx.author.id] = number
    await ctx.send("Pick a number from 1 to 20.")

@bot.command()
async def score(ctx):
    score = user_scores.get(ctx.author.id, 0)
    await ctx.send(f'Your score is: {score}')

@bot.event
async def on_message(message):
    await bot.process_commands(message)

    if message.author.bot:
        return

    user_id = message.author.id

    if user_id in active_numbers:
        try:
            guess = int(message.content)
        except ValueError:
            return 

        correct = active_numbers[user_id]
        if guess == correct:
            await message.channel.send("Correct.")

            # Update score
            user_scores[user_id] = user_scores.get(user_id, 0) + 1
        else:
            await message.channel.send("Incorrect. Retry?")

bot.run()

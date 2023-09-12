import discord
import os
import requests
import random
from pasword import gen_pass
from discord.ext import commands

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

intents = discord.Intents.all()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def call1(ctx, a: int, b: int):
    await ctx.send(a + b)

@bot.command()
async def call2(ctx, a: int, b: int):
    await ctx.send(a - b)

@bot.command()
async def call3(ctx, a: int, b: int):
    await ctx.send(a * b)

@bot.command()
async def call4(ctx, a: int, b: int):
    await ctx.send(a // b)

@bot.command()
async def callt(ctx, a: int, b: int):
    await ctx.send(a / b)

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def meme(ctx):
    all_mems = os.listdir("images")
    rand_mem = random.choice(all_mems)
    with open(f"images/{rand_mem}", 'rb') as f:
        imagesd = discord.File(f)
    await ctx.send(file=imagesd)

@bot.command()
async def ameme(ctx):
    all_amems = os.listdir("Ameme")
    rand_amem = random.choice(all_amems)
    with open(f"Ameme/{rand_amem}", 'rb') as f:
        Ameme = discord.File(f)
    await ctx.send(file=Ameme)

bot.run("HER'S THE TOKEN")
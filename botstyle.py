import discord
from discord.ext import commands
from discord.ext.commands import bot
import asyncio
import os

bot = commands.Bot(command_prefix='#')
client = discord.Client()

@bot.event
async def on_ready():
    print ("ready for use, just gunna add a happy syntax error here")
    print (bot.user.id)

@bot.command(pass_context=True)
async def meme(ctx):
    await bot.say("I like memes")



@bot.group(pass_context=True)
async def neural(ctx):
    if ctx.invoked_subcommand is None:
        await bot.say('Invalid git command passed...')

@neural.command()
async def style(ncontent: str, styles: str, name: str):
    await bot.say('neural style {} {} {}'.format(ncontent, styles, name))
    os.system("python neural_style.py --content {} --styles {} --output {} --width 500".format(ncontent, styles, name))

#img = input("content enter hal9000.png:")
#pic = input("style enter bob.jpg:")
#name = input("name enter name of new file .png:")

#os.system("python neural_style.py --content " + img +" --styles " + pic +" --output " + name +" --width 500")


bot.run("NDQ0NTAxMzc3NjU4NjUwNjUz.DeOtQA.kvh4om4oBfHQjcRUZOVhH5fc4Ps")

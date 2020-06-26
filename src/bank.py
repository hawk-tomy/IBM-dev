import logging
import os
import sys

import discord
from discord.ext import commands
import yaml

#import pack.util
from pack.util import myfunction as MF

MF.getLogger('discord', level=logging.WARNING, saveName='main.log',path='log')
logger = MF.getLogger('bot', saveName='main.log',path='log')

with open('token','r',encoding='utf-8')as f:
    TOKEN = f.read()
bot = commands.Bot(command_prefix= '/')


@bot.event
async def on_ready():
    logger.info('login success')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def kill(ctx):
    await ctx.send('killing now...')
    print('killing now...')
    await sys.exit()

@bot.command()
async def restart(ctx):
    await ctx.send('resatrt now...')
    print('restart now...')
    os.execl(sys.executable, os.path.abspath(__file__), os.path.abspath(__file__))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

bot.run(TOKEN)

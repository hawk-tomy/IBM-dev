import logging

import discord
from discord.ext import commands
import yaml

import myfunction as MF

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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

bot.run(TOKEN)

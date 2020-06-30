import logging
import os
import sys

import discord
from discord.ext import commands
import yaml

import src.bank.account as account
import src.bank.admin as admin
import src.util.help as help
from src.util import myfunction as MF

MF.getLogger('discord', level=logging.WARNING, saveName='main.log',path='log')
logger = MF.getLogger('bot', saveName='main.log',path='log')

with open('token','r',encoding='utf-8')as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix= '/',help_command=help.Help(),description="")
account.setup(bot)
admin.setup(bot)

@bot.event
async def on_ready():
    logger.info('login success')

@bot.command()
async def kill(ctx):
    await ctx.send('killing now...')
    logger.info('killing now...')
    await sys.exit()

@bot.command()
async def restart(ctx):
    await ctx.send('resatrt now...')
    logger.info('restart now...')
    os.execl(sys.executable, os.path.abspath(__file__), os.path.abspath(__file__))

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

bot.run(TOKEN)

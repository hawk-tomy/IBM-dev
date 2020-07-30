import logging
import os
import sys

import discord
from discord.ext import commands
import yaml

import src.util.help as help
import src.util as MF
import src.bank
import src.IBM

MF.getLogger('discord', level=logging.WARNING, saveName='main.log',path='log')
logger = MF.getLogger('bot', saveName='main.log',path='log')

with open('data/data.yaml','r',encoding='utf-8')as f:
    data = yaml.safe_load(f)
with open('data/config.cfg','r',encoding='utf-8')as f:
    config = yaml.safe_load(f)
with open('token','r',encoding='utf-8')as f:
    TOKEN = f.read()

bot = commands.Bot(command_prefix= '/',help_command=help.Help(),description="")
bot.add_cog(Account(bot))
bot.add_cog(Admin(bot, data, config))

@bot.event
async def on_ready():
    logger.info('login success')

@bot.command()
@commands.is_owner()
async def kill(ctx):
    await ctx.send('killing now...')
    logger.info('killing now...')
    await sys.exit()

@bot.command()
@commands.is_owner()
async def restart(ctx):
    await ctx.send('resatrt now...')
    logger.info('restart now...')
    os.execl(sys.executable, os.path.abspath(__file__), os.path.abspath(__file__))

@bot.command()
@commands.is_owner()
async def reload(ctx):
    bot.remove_cog('Account')
    bot.remove_cog('Admin')
    bot.add_cog(Account(bot))
    bot.add_cog(Admin(bot, data, config))
    logger.info('reload succes')
    await ctx.send('reload success')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    if isinstance(error, commands.NotOwner):
        return
    raise error

bot.run(TOKEN)

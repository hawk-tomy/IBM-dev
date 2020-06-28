import logging
import os
import sys

import discord
from discord.ext import commands
import yaml

from pack.util import myfunction as MF

logger = logging.getLogger('bot').getChild(__name__)

class Account(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')
        logger.info('ping&pong')

    @commands.command(name= 'in')
    async def _in(self, ctx):
        await ctx.send('in')
        logger.info('in')

    @commands.command()
    async def out(self, ctx):
        await ctx.send('out')
        logger.info('out')

    @commands.group()
    async def show(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('show')
            logger.info('show')

    @show.command()
    async def deposit(self, ctx):
        await ctx.send('show deposit')
        logger.info('show deposit')

    @show.command()
    async def log(self, ctx):
        await ctx.send('log')
        logger.info('log')

def setup(bot):
    bot.add_cog(Account(bot))
    logger.info('add_cog_success')

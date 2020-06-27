import logging

import discord
from discord.ext import commands
import yaml

from pack.util import myfunction as MF

logger = logging.getLogger('bot').getChild('bank.user')

class User(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')
        logger.info('ping&pong')
    
    @commands.command()
    async def in(self, ctx):
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
        ctx.send('log')
        logger.info('log')

def setup(bot):
    bot.add_cog(User(bot))
    logger.info('add_cog_success')

import logging

import discord
from discord.ext import commands
import yaml

from src.util import myfunction as MF

logger = logging.getLogger('bot').getChild(__name__)

class Admin(commands.Cog):
    '''
    Admin
    '''
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def show(self, ctx):
        '''show
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('show')
            logger.info('show')

    @commands.group()
    async def settings(self, ctx):
        '''settings
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('settings')
            logger.info('settings')

    @commands.group()
    async def bank(self, ctx):
        '''bank
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('bank')
            logger.info('bank')

    @commands.group()
    @commands.has_permissions(administrator=True)
    async def make(self,ctx)
        if ctx,invoked_subcommand is None:
            await ctx.send('make')
            logger.info('make')

def setup(bot):
    bot.add_cog(Admin(bot))
    logger.info('add_cog_success')

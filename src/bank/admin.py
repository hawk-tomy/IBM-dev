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

    @commands.command()
    async def ping(self, ctx):
        '''
        test
        '''
        await ctx.send('pong')
        logger.info('ping')

    @commands.command()
    async def niconico(self, ctx):
        '''
        niconico
        '''
        await ctx.send('^^')
        logger.info('niconico')

def setup(bot):
    bot.add_cog(Admin(bot))
    logger.info('add_cog_success')

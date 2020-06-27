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

def setup(bot):
    bot.add_cog(User(bot))
    logger.info('add_cog_success')

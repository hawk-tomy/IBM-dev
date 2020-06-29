import logging

import discord
from discord.ext import commnads
import yaml

from pack.util import myfunction as MF

logger = logging.getLogger('bot').getChild(__name__)

class Admin(comannds.cog):
    
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Admin(bot))
    logger.info('add_cog_success')
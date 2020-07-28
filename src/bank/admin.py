import logging
import os
import re

import discord
from discord.ext import commands
import yaml

from src.util import myfunction as MF

logger = logging.getLogger('bot').getChild(__name__)

class Admin(commands.Cog):
    '''
    Admin
    '''
    def __init__(self, bot, data, config):
        logger.info('add_cog_success')
        self.bot = bot
        self.data = data
        self.config = config

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

    @bank.group()
    async def show(self, ctx):
        '''show
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('show')
            logger.info('show')

    @bank.command()
    @commands.has_permissions(administrator=True)
    async def make(self, ctx, *, arg):
        if re.search(r'[\\/:*?"<>|]',arg):
            await ctx.send('使用不可能な文字が含まれています。`\/:*?"<>|`以外を使用してください。')
        else:
            self.data['bank_index'] = {ctx.guild.id: str(arg)}
            with open('data/data.yaml','w',encoding='utf-8')as f:
                yaml.dump(self.data, f, encoding='utf-8', allow_unicode=True)
            os.mkdir('data/' + str(arg))

            await ctx.send('make : '+ str(arg))
            logger.info('make :' + str(arg))

    @make.error
    async def make_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('コマンドを実行するための権限が足りません')

def setup(bot):
    bot.add_cog(Admin(bot))

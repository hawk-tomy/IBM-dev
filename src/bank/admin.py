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
    async def setup(self, ctx):
        '''setup
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('<<setup tools help>>')
            logger.info('setup')

    @commands.group()
    async def bank(self,ctx):
        """bank
        """
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

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def start(self,ctx)
        """setup start
        """
        await ctx.send('<<setup tools>>¥nstart setup bot. please use command "'+ctx.prefix+'setup make"')
        logger.info('start_setup')

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def make(self, ctx, *, arg):
        """setup make bank
        """
        if ctx.guild.id in list(self.data['bank'].keys()):
            ctx.send('このサーバーに銀行は設立されています。')
            return
        self.data['bank'] += {ctx.guild.id: {'full_bank_name': str(arg)}}
        with open('data/data.yaml','w',encoding='utf-8')as f:
            yaml.dump(self.data, f, encoding='utf-8')

        await ctx.send('「'+str(arg)+'」を作成しました。¥nNext command is setup shortname')
        logger.info('setup_make_bank - bank_name :' + str(arg) + 'usedby' +userinfo())

    @setup.command()
    @commands.has_permissions(administrator=True)
    async def shortname(self, ctx, *, arg):
        if not ctx.guild.id in data['bank']:
            await ctx.send('This Guild Not Has Bank.\nPrease Used Command "setup make [bank name]"')
            return
        data['bank'][ctx.guild.id]['shortname'] = args
        await ctx.send(arg + 'に設定しました。')
        logger.info('setup_set_short_name_is_succes Usedby : ' + userinfo())

    @make.error
    async def make_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send('コマンドを実行するための権限が足りません')

def userinfo(ctx):
    retrun ctx.author.name + ' - ' + ctx.author.id

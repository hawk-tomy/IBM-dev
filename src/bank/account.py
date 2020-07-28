import logging

import discord
from discord.ext import commands
import yaml

from src.util import myfunction as MF

root= logging.getLogger('bot')
logger = root.getChild(__name__)

class Account(commands.Cog):
    '''口座操作系コマンド一覧
    テスト1
    テスト2
    テスト3
    テスト4
    '''

    def __init__(self, bot):
        logger.info('add_cog_success')
        self.bot = bot

    @commands.command(name= 'in')
    async def _in(self, ctx):
        '''
        入金コマンドです。
        '''
        await ctx.send('in')
        logger.info('in')

    @commands.command()
    async def out(self, ctx):
        '''出金コマンドです。
        '''
        await ctx.send('out')
        logger.info('out')

    @commands.command()
    async def send(self, ctx):
        '''送金コマンドです。
        '''
        await ctx.send('send')
        logger.info('send')

    @commands.group()
    async def show(self, ctx):
        '''各種データを確認できます。
        '''
        if ctx.invoked_subcommand is None:
            await ctx.send('show')
            logger.info('show')

    @show.command()
    async def deposit(self, ctx):
        '''預金額を確認できます。
        '''
        await ctx.send('show deposit')
        logger.info('show deposit')

    @show.command()
    async def log(self, ctx):
        '''ログを確認できます。
        '''
        await ctx.send('log')
        logger.info('log')

def setup(bot):
    bot.add_cog(Account(bot))

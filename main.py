import logging

import discord
import yaml

import myfunction as MF

MF.getLogger('discord', level=logging.WARNING, saveName='main.log',path='log')
logger = MF.getLogger('bot', saveName='main.log',path='log')

with open('token','r',encoding='utf-8')as f:
    TOKEN = f.read()
client = discord.Client()


BoBadmin = []
BoBuser = []
Bankadmin = []
Currency = []
user = ['in','out','show']
usershow = []

@client.event
async def on_ready():
    logger.info('login success')

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.content == '/neko':
        await message.channel.send('にゃーん')

client.run(TOKEN)

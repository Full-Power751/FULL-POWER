import discord
from discord.ext import commands
import random
import asyncio
import time
from datetime import datetime
import sys
import os
import traceback
from discord.ext.commands import bot, cog

 
client = commands.Bot (command_prefix = 'f!')


@client.command()
async def hello(ctx):
    await ctx.send('Hi')

@client.command()
async def verison(ctx):
    await ctx.send('1.0.0')

@client.command()
async def BG(ctx):
    await ctx.send('Bhai Gamer')

@client.command()
async def Legend(ctx):
    await ctx.send('Legend is always op')

@client.command()
async def op(ctx):
    await ctx.send('Over Power')

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):             
    await member.kick(reason=reason)
    await ctx.send(f'{member.name} was successfully kick. {reason}')

@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please mention a user to kick.')


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):             
    await member.ban(reason=reason)
    await ctx.send(f'{member.name} was successfully banned. {reason}')
    

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('f!help'))
    print('Full Power is now online')

@client.command()
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)


@commands.command()
async def guild_icon(self, ctx):
        mbed = discord.Embed()
        mbed.set_image(url = ctx.guild.icon_url)
        await ctx.send(embed=mbed)

@client.command()
async def txdeletechannel(ctx, channel: discord.TextChannel):
    mbed = discord.Embed(

        title = 'Success',
        description = f'Channel: {channel} has been deleted',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()


@client.command()
async def vcdeletechannel(ctx, channel: discord.VoiceChannel):
    mbed = discord.Embed(

        title = 'Success',
        description = f'Channel: {channel} has been deleted',
    )
    if ctx.author.guild_permissions.manage_channels:
        await ctx.send(embed=mbed)
        await channel.delete()


@client.command()
async def createchannel(ctx, channelName):
    guild = ctx.guild

    mbed = discord.Embed(
        title = 'Success',
        description = "{} has been created successfully.".format(channelName)
    )
    if ctx.author.guild_permissions.manage_channels:
        await guild.create_text_channel(name='{}'.format(channelName))
        await ctx.send(embed=mbed)









client.run('ODM3NjY3MTU1OTc3ODMwNDAw.YIv4VQ.D7comK0LwuyGJfvatMqhyv0zaQE')
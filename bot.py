import discord
from discord.ext import commands
from discord import guild
from discord import colour
from discord import channel
from io import BytesIO
import random
import asyncio
import time
from datetime import datetime
import sys
import os
import traceback
import DiscordUtils
import json
from DiscordUtils.Music import Song
from discord.ext.commands.converter import clean_content
from discord.ext.commands.core import guild_only
from discord.flags import Intents
from discord_slash import SlashCommand
import youtube_dl

Intents = discord.Intents().all()
client = commands.Bot(command_prefix = 'f!')
slash = SlashCommand(client, sync_commands=True)
music = DiscordUtils.Music()


@client.event
async def on_ready():
    print("I am Online")
    await client.change_presence(activity= discord.Streaming(name = "24/7 Online", url = "https://www.twitch.tv/ishitwa"))


@slash.slash(description='Shows Userinfo')            
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.colour)

    embed.set_author(name=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Guild name:", value=member.display_name)
    embed.add_field(name="Account Created at:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined The Server at:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name=f"Roles ({len(roles)})", value="".join([role.mention for role in roles]))
    embed.add_field(name="Top role:", value=member.top_role.mention)
    embed.add_field(name="Bot?",value=member.bot)

    await ctx.send(embed=embed)

@client.command()           
async def about(ctx):

    embed = discord.Embed(colour=0x00FFFCC)

    embed.set_author(name="Bot Info")
    embed.set_thumbnail(url="https://cdn.discordapp.com/avatars/837667155977830400/a8961ad6b0025423f791f189da1e7b1a.png?size=256")
    embed.add_field(name="Developed by", value="``𝗫10乛Ishitwa#0001``", inline=False)
    embed.add_field(name="Developed in", value="Python Version ``3.9.5``", inline=False)
    embed.add_field(name="**Support Server**", value="||https://discord.gg/BvUMxhTn||", inline=False)
    embed.add_field(name="Invite Link", value="||https://discord.com/api/oauth2/authorize?client_id=837667155977830400&permissions=8&scope=bot%20applications.commands||", inline=False)

    await ctx.send(embed=embed)

@client.command()
async def serverinfo(ctx):
    embed = discord.Embed(title='Server Info', color=0xf14645)
    embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
    embed.add_field(name="Server Name", value=ctx.guild.name, inline=False)
    embed.add_field(name="Server Owner", value=ctx.guild.owner.display_name, inline=False)
    embed.add_field(name="Creation Date", value=ctx.guild.created_at.strftime("%a, %d %B %Y, %I:%M %p"), inline=False)
    embed.add_field(name="Members", value=len(ctx.guild.members), inline=False)
    embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=False)
    embed.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=embed)


@slash.slash(description='Show ping')
async def ping(ctx):
    await ctx.send(f'Bot Speed - {round(client.latency * 1000)}ms')   

@slash.slash(description='Give role')
@commands.has_permissions(administrator=True)
async def role(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)
        await ctx.send(f"Successfully given {role.mention} to {user.mention}.")

@client.command()
async def join(ctx):
    await ctx.author.voice.channel.connect()
    await ctx.send(f'**Joined Your Voice Channel <a:tick:883640082848968704>**')


extensions=['cogs.dm',
            'cogs.avatar',
            'cogs.moderation'
]           
if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:  
            print(f'Error loading {extension}', file=sys.stderr)
            traceback.print_exc('Cannot load')  
            

client.run('ODM3NjY3MTU1OTc3ODMwNDAw.YIv4VQ.D7comK0LwuyGJfvatMqhyv0zaQE')
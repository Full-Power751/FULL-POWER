import discord
from discord.ext import commands
import random
import asyncio
import time
from datetime import datetime
import sys
import os
import traceback
from discord.ext.commands import bot

 
client = commands.Bot (command_prefix = 'f!')


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):             
    await member.kick(reason=reason)
    embed = discord.Embed(

        description = f"{member} was successfully Kicked.",        
    )    
    await ctx.send(embed=embed)
    
@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please mention a user to Kick.')

@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description=f"You do not have Permission to kick members. ")
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):             
    await member.ban(reason=reason)
    embed = discord.Embed(

        description = f"{member} was successfully Kicked.",
        
    )    
    await ctx.send(embed=embed)
    
@kick.error
async def kick_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please mention a user to Ban.')  

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Updated Successfully to Version 1.5.0'))
    print('Full Power is now online')

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, ammount: int):
    await ctx.channel.purge(limit=ammount+1)
    embed = discord.Embed(description=f"I have cleared {ammount} messages.")
    await ctx.send(embed=embed)
     
@clear.error
async def clear_error(ctx , error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(description="Please specify the number of messages to clear.")
        await ctx.send(embed=embed)

@clear.error
async def clear_error(ctx , error):
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(description="You are missing a following permission Manage Messages.")
        await ctx.send(embed=embed)

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
        
@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member = ctx.author if not member else member
    roles = [role for role in member.roles]

    embed = discord.Embed(colour=member.colour, timestamp=ctx.message.created_at)

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
@commands.has_permissions(administrator=True)
async def role(ctx, role: discord.Role, user: discord.Member):
    if ctx.author.guild_permissions.administrator:
        await user.add_roles(role)
        await ctx.send(f"Successfully given {role.mention} to {user.mention}.")
        
@client.command(description="Mutes the specified user.")
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member, *, reason=None):
    guild = ctx.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")

    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")

        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, view_channel=None, send_messages=False, connect=False, read_message_history=True, read_messages=False)

    await member.add_roles(mutedRole, reason=reason)
    await ctx.send(f"Muted {member.mention} for reason {reason}")
    await member.send(f"You were muted in the server {guild.name} for {reason}")

@client.command(description="Unmutes a specified user.")
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    await ctx.send(f"Unmuted {member.mention}")
    await member.send(f"You were unmuted in the server {ctx.guild.name}")


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.kick(reason=f'Kicked By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Successfully Kicked {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Please Provide A Member To Kick...`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)
    else:
        await member.kick(reason=reason)
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Successfully Kicked {member} For {reason}.`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member = None, *, reason = None):
    if reason == None:
        await member.ban(reason=f'Banned By {ctx.author} With No Reason Provided...')
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Successfully Banned {member} With No Reason Provided.`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)
    if member == None:
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Please Provide A Member To Ban...`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)
    else:
        await member.ban(reason=reason)
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Successfully Banned {member} For {reason}.`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)

@client.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, member_id = None):
    if member_id == None:
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Please Provide A Member ID To Unban...`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)
    else:
        await ctx.guild.unban(user=member_id)
        embed = discord.Embed(title='Full Power', color=0x19dfb8, description=f'**`Successfully Unbanned {member_id}!`**')
        embed.set_thumbnail(url='https://cdn.dribbble.com/users/344048/screenshots/4134234/bot_icon_dribbble.jpg')
        await ctx.send(embed=embed)

extensions=['cogs.dm',
            'cogs.avatar'
]           
if __name__ == "__main__":
    for extension in extensions:
        try:
            client.load_extension(extension)
        except Exception as e:  
            print(f'Error loading {extension}', file=sys.stderr)
            traceback.print_exc('Cannot load')  
            

client.run('ODM3NjY3MTU1OTc3ODMwNDAw.YIv4VQ.D7comK0LwuyGJfvatMqhyv0zaQE')
import re
import datetime
from copy import deepcopy

import asyncio
import discord
from discord.ext import commands, tasks
from dateutil.relativedelta import relativedelta

time_regex = re.compile("(?:(\d{1,5})(h|s|m|d))+?")
time_dict = {"h": 3600, "s": 1, "m": 60, "d": 86400}



class Moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.mute_task = self.check_current_mutes.start()

    def cog_unload(self):
        self.mute_task.cancel()


    @commands.command(
        name="kick",
        description="A command which kicks a given user",
        usage="<user> [reason]",
    )
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.kick(user=member, reason=reason)

        embed = discord.Embed(
            description=f"Seccessfully Kicked {member.mention}"

        )
        
             
        await ctx.send(embed=embed)

    @commands.command(
        name="ban",
        description="A command which bans a given user",
        usage="<user> [reason]",
    )
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *, reason=None):
        await ctx.guild.ban(user=member, reason=reason)

        
        embed = discord.Embed(
            title=f"{ctx.author.name} banned: {member.name}", description=reason
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="unban",
        description="A command which unbans a given user",
        usage="<user> [reason]",
    )
    @commands.guild_only()
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member, *, reason=None):
        member = await self.bot.fetch_user(int(member))
        await ctx.guild.unban(member, reason=reason)

        embed = discord.Embed(
            title=f"{ctx.author.name} unbanned: {member.name}", description=reason
        )
        await ctx.send(embed=embed)

    @commands.command(
        name="purge",
        description="A command which purges the channel it is called in",
        usage="[amount]",
    )
    @commands.guild_only()
    @commands.is_owner()
    async def purge(self, ctx, amount=15):
        await ctx.channel.purge(limit=amount + 1)
        embed = discord.Embed(
            title=f"{ctx.author.name} purged: {ctx.channel.name}",
            description=f"{amount} messages were cleared",
        )
        await ctx.send(embed=embed, delete_after=15)


def setup(bot):
    bot.add_cog(Moderation(bot))
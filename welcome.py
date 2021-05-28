import discord
from discord.ext import commands
from discord.utils import get


class Welcome(commands.Cog, name='Welcomer') :

    def _init_(self,bot):
        self.bot = bot


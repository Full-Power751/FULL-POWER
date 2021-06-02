import discord
from discord.ext import commands


class DM(commands.Cog):
    def __init__(self,bot):
        self.bot = bot



    @commands.command()
    async def dm(self,ctx,user: discord.Member,*,args):
        if args != None:
            try:
                await user.send(args)
                await ctx.send(f'DM sent to {user.name}')
            except:
                    await ctx.send('User has closed his DM')



def setup(bot):
    bot.add_cog(DM(bot))                        

import discord
from discord.ext import commands
import os

"""
DO NOT DELETE THIS FILE AS THIS IS THE MAIN FILE
RELOAD, UNLOAD, LOAD PACKAGES
"""

class Core:
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def reload(self, ctx, cog:str=None):
        if cog == None or cog == " ":
            return await ctx.send("Invalid cog name!\n```\nUsage: ./reload cogs.<cog name>\n```")
        try:
            await ctx.send("Reloading extension...")
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            await ctx.send("Successfully loaded extension!")
        except Exception as e:
            return await ctx.send(f"Failed to reload extension:\n```\n{e}\n```")
        
def setup(bot):
    bot.add_cog(Core(bot))
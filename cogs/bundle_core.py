import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isfile, join

"""
DO NOT DELETE THIS FILE AS THIS IS THE MAIN FILE
RELOAD, UNLOAD, LOAD PACKAGES
"""

class Core:
    def __init__(self, bot):
        self.bot = bot

        self.cog_search()

    def cog_search(self):
        self.cogs = []

        # Finds current path and finds all files in cogs directory
        mypath = str(os.path.dirname(os.path.abspath(__file__)))
        cogpath = [f for f in listdir(mypath) if isfile(join(mypath, f))]

        # Add them to cogs list 
        for file in cogpath:
            file = "cogs.{}".format(file).replace(".py", "")
            self.cogs.append(file)
    
    @commands.command()
    async def list_cog(self, ctx):
        list_ = ""
        for cog in self.cogs:
            list_ += "{}\n".format(cog)
        return await ctx.send(f"```css\n{list_}\n```")

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
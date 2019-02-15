import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isfile, join
import subprocess
import sys

class Package:
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command()
    async def install(self, ctx, url:str=None):
        if url == "" or url == " " or url == None:
            return await ctx.send("Invalid url!")
        try:
            await ctx.send(f"Starting to install cog...")
            os.system(f"cd cogs && git clone {url}")
            await ctx.send("Cloned repository cog...")
            #await ctx.send("Trying to find cog file...")
            #os.system(f"cd cog")
        except Exception as e:
            return await ctx.send(f"Error installing cog...please contact the developer for help! Details: ```{e}```")
        await ctx.send("Successfully installed cog!")

def setup(bot):
    bot.add_cog(Package(bot))
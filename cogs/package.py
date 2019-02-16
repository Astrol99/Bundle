import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isfile, join
import subprocess
import sys

"""
MAIN FILE TO INSTALL AND UNINSTALL COGS
DO NOT DELETE!!!
"""

class Package:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def install(self, ctx, url:str=None):
        # Checks if user input is right so it doesn't install wrong files
        if url == "" or url == " " or url == None:
            return await ctx.send("Invalid url!")
        elif url[:18] != "https://github.com":
            return await ctx.send("Invalid url!")
        try:
            # Splits the url by slashes
            self.name_repo = url.split("/")
            # Gets name of the repo and deletes the ".git"
            self.name_repo = self.name_repo[4].replace(".git", "")
            await ctx.send(f"Starting to install {self.name_repo}...")
            # Goes into cogs directory then git clones the url
            os.system(f"cd cogs && git clone {url}")
            await ctx.send("Cloned repository cog...")
            await ctx.send("Trying to find cog file and moving it...")
            # Goes into the cloned repo then moves the main cog file into cog/ directory
            os.system(f"cd cogs/{self.name_repo};mv {self.name_repo}.py ../")
            await ctx.send("Cleaning up...")
            # Deletes the repo so it only takes the main cog file
            os.system(f"cd cogs;rm -r -rf {self.name_repo}")
            await ctx.send("Automatically loading cog...")
            # 
            self.bot.load_extension(f"cogs.{self.name_repo}")
            await ctx.send("Successfully installed cog!")
        except Exception as e:
            return await ctx.send(f"Error installing cog...please contact the developer for help! Details: ```{e}```")

def setup(bot):
    bot.add_cog(Package(bot))
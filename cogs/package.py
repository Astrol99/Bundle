import discord
from discord.ext import commands
import os
from os import listdir
from os.path import isfile, join
import subprocess
import sys

"""
NOTE: The only install cogs that has the file and repo name as the same
~ Unless there was another way I couldn't think of...

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
            return await ctx.send("Invalid url! - Usage: ./install <git repo url>")
        elif url[:18] != "https://github.com":
            return await ctx.send("Invalid url! - Usage: ./install <git repo url>")
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
            # Auto reloads cog right after it's installed
            self.bot.load_extension(f"cogs.{self.name_repo}")
            await ctx.send("Successfully installed cog!")
        except Exception as e:
            return await ctx.send(f"Error installing cog...please contact the developer for help! Details: ```{e}```")
    
    @commands.command()
    async def uninstall(self, ctx, cog:str=None):
        error_msg = "Unvalid cog name! - Usage: ./uninstall cogs.<cogname>"
        if cog == " " or cog == None:
            return await ctx.send(error_msg)
        elif cog[:3] != "cog":
            return await ctx.send(error_msg)
        try:
            # Why does line 57 exist? Just to keep consistancy with "cogs." to not confuse end-user
            cog = cog.replace("cogs.", "").replace(" ", "")
            # Unloads extension so it doesn't interfere with live bot
            await ctx.send("Unloading extension first...")
            self.bot.unload_extension(f"cogs.{cog}")
            # Goes into directory and deletes the cog
            await ctx.send("Uninstalling cog...")
            os.system(f"cd cogs; rm {cog}.py")
            await ctx.send(f"Successfully uninstalled {cog}")
        except Exception as e:
            return await ctx.send(f"Error uninstalling cog!```{e}```")

def setup(bot):
    bot.add_cog(Package(bot))
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
        elif url[:18] != "https://github.com":
            return await ctx.send("Invalid url!")
        try:
            self.name_repo = url.split("/")
            self.name_repo = self.name_repo[4].replace(".git", "")
            await ctx.send(f"Starting to install {self.name_repo}...")
            os.system(f"cd cogs && git clone {url}")
            await ctx.send("Cloned repository cog...")
            await ctx.send("Trying to find cog file and moving it...")
            os.system(f"cd cogs/{self.name_repo};mv {self.name_repo}.py ../")
            await ctx.send("Cleaning up...")
            os.system(f"cd cogs;rm -r -rf {self.name_repo}")
            await ctx.send("Automatically loading cog...")
            self.bot.load_extension(f"cogs.{self.name_repo}")
            await ctx.send("Successfully installed cog!")
        except Exception as e:
            return await ctx.send(f"Error installing cog...please contact the developer for help! Details: ```{e}```")

def setup(bot):
    bot.add_cog(Package(bot))
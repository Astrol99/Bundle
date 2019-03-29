import discord
from discord import Member
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
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

class Package(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        # Make sure user doesn't uninstall main packagess since it will break the bot
        self.important_cogs = [
            "cogs.bundle_core",
            "cogs.package",
            "cogs.error_handle"
        ]

    def cmd_run(self, command):
        if " " in command:
            command = command.split(" ")
        subprocess.run(command, shell=True, stdin=subprocess.PIPE, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)

    @commands.command()
    @has_permissions(administrator=True) # Checks if the user is an admin in that server
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
            print(f"\n[!] Starting to install {self.name_repo}...")
            # Goes into cogs directory then git clones the url
            print(f"[*] Clonning {self.name_repo}")
            if os.name == "nt":
                self.cmd_run(f"cd cogs && git clone {url}")
            else:
                self.cmd_run(f"cd cogs ; git clone {url}")
            await ctx.send("Cloned repository cog...")
            await ctx.send("Trying to find cog file and moving it...")
            print("[*] Cloned repository cog...")
            print("[*] Trying to find cog file and moving it...")
            # Goes into the cloned repo then moves the main cog file into cog/ directory
            if os.name == "nt":
                self.cmd_run(f"cd cogs/{self.name_repo} && move {self.name_repo}.py ../")
            else:
                self.cmd_run(f"cd cogs/{self.name_repo} ; mv {self.name_repo}.py ../")
            await ctx.send("Cleaning up...")
            print("[*] Cleaning up...")
            # Deletes the repo so it only takes the main cog file
            if os.name == "nt":
                # Finds current path and finds all files in cogs directory
                self.mypath = str(os.path.dirname(os.path.abspath(__file__))) + f"\{self.name_repo}"
                self.cogpath = [f for f in listdir(self.mypath) if isfile(join(self.mypath, f))]
                for item in self.cogpath:
                    os.system(f"cd cogs/{self.name_repo} && del {item}")
                os.system(f"cd cogs/ && rmdir /Q /S {self.name_repo}")
            else:
                os.system(f"cd cogs ; rm -r -rf {self.name_repo}")
            await ctx.send("Automatically loading cog...")
            print("[*] Automatically loading cog...")
            # Auto reloads cog right after it's installed
            self.bot.load_extension(f"cogs.{self.name_repo}")
            print("[!] Successfully installed cog!")
            await ctx.send("Successfully installed cog!")
        except Exception as e:
            print(f"[!] Failed to install {self.name_repo}! -> {e}")
            return await ctx.send(f"Error installing cog...please contact the developer for help! Details: ```{e}```")

    @commands.command()
    @has_permissions(administrator=True)
    async def uninstall(self, ctx, cog:str=None):
        error_msg = "Invalid cog name! - Usage: ./uninstall cogs.<cogname>"
        if cog == " " or cog == None:
            return await ctx.send(error_msg)
        elif cog[:3] != "cog":
            return await ctx.send(error_msg)
        elif cog in self.important_cogs:
            return await ctx.send("Unable to delete main files!")
        try:
            # Why does line 57 exist? Just to keep consistancy with "cogs." to not confuse end-user
            cog = cog.replace("cogs.", "").replace(" ", "")
            # Unloads extension so it doesn't interfere with live bot
            await ctx.send("Unloading extension first...")
            self.bot.unload_extension(f"cogs.{cog}")
            # Goes into directory and deletes the cog
            await ctx.send("Uninstalling cog...")
            if os.name == "nt":
                os.system(f"cd cogs && del {cog}.py")
            else:
                os.system(f"cd cogs ; rm {cog}.py")
            await ctx.send(f"Successfully uninstalled {cog}")
        except Exception as e:
            return await ctx.send(f"Error uninstalling cog!```{e}```")

    # These functions are executed if the user that attempted to use install command isn't a admin
    @install.error
    async def install_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
        # Main message sented to user that executed command
            msg = "Sorry {}, you don't have admin privilages to install packages!".format(ctx.message.author)
            await ctx.send(msg)

    @uninstall.error
    async def uninstall_error(self, error, ctx):
        if isinstance(error, MissingPermissions):
            msg = "Sorry {}, you don't have admin privilages to uninstall packages!".format(ctx.message.author)
            await ctx.send(msg)

def setup(bot):
    bot.add_cog(Package(bot))

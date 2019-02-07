import discord
from discord.ext import commands
import sys
import colorama
from colorama import Fore, Style
import os
from os import listdir
from os.path import isfile, join

# To allow windows users to see colors
colorama.init(convert=True, autoreset=True)

# MAKE SURE TO MAKE YOUR OWN TOKEN.TXT 
# Opens token.txt to extract TOKEN
with open("token.txt") as f:
	char0 = f.readlines()
	TOKEN = char0[0]
	f.close()

# Checks if TOKEN is valid, if not, exits out
if TOKEN[0] != "N":
	print(f"{Fore.RED}[!] Unable to launch - No Token\nExiting...")
	sys.exit(0)

cogs = []

# Finds current path and finds all files in cogs directory
mypath = str(os.path.dirname(os.path.abspath(__file__))) + "\cogs"
cogpath = [f for f in listdir(mypath) if isfile(join(mypath, f))]

# Add them to cogs list 
for file in cogpath:
	file = "cogs.{}".format(file).replace(".py", "")
	cogs.append(file)

# User ID for permissions such as shutting down bot
# Current one is mine so you can replace it with yours
dev = [354693078495264778]

bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
	# Welcome message when launching bot
	msg = """
{}__________________________________
|/////////////////////////////////|
{}|       Welcome To Bundle!        |
|/////////////////////////////////|
***********************************
""".format(Fore.BLUE,Fore.LIGHTYELLOW_EX)
	print(msg)
	print("~ A discord cogs package manager :)\n")
	# Pretty messy but gets the job done
	print(f"[!] Status: {Fore.GREEN}Online!")
	print(f"[/] Signed in as: {Fore.YELLOW}{bot.user}") 
	print(f"[/] Servers Connected: {Fore.MAGENTA}{len(bot.guilds)}\n")

# Command to shutdown bot cleanly
@bot.command()
async def shutdown(ctx):
	# Checks if users ID is in dev list
	if ctx.author.id not in dev:
		return await ctx.send("Hol'up, you ain't a dev")
	await ctx.send("Shutting down...")
	await bot.logout()

# Loads all cogs in cog list when launched
if __name__ == "__main__":
	if not cogs:
		print(f"{Fore.RED}[>] No cogs available, skipping cog initialization...")
	else:
		print(f"{Style.DIM}[~] Initializing cogs...")
		for cog in cogs:
			try:
				bot.load_extension(cog)
				print(f"{Fore.GREEN}[*] Successfully loaded {Fore.YELLOW}{cog}")
			except Exception as e:
				print(f"{Fore.RED}[*] Unable to load {Fore.YELLOW}{cog}{Fore.WHITE}: {e}")
		print(f"[~] Finished loading cogs!\n[/] Switched to monitoring mode...have a nice day!")

bot.run(TOKEN)

import sys
import os
try: # Checks if discord is installed on end-users machine
	import discord
except ImportError:
	print("[!] You don't have discord installed!")
	msg = "[/] Would you like to install discord 1.0.0a now?(Y/n): "
	install_rewrite = input(msg)
	if install_rewrite.lower() == "y":
		print("[*] Preparing to install...")
		os.system("pip3 install -U git+https://github.com/Rapptz/discord.py@rewrite#egg=discord.py[voice]") # Does a pip installation through command line
		print("\n[!] Finished! ~ Please launch the bot again. Exiting...")
		sys.exit(0) 
	# Just exits if the user says no
	elif install_rewrite.lower() == "n":
		print("[!] Exiting...")
		sys.exit(0)
	else:
		print("[*] Invalid answer - it has to be 'y' or 'n' ~ Exiting...")
		sys.exit(0)
# This portion is to check if it has the right version
version = discord.__version__
if version != "1.0.0a":
	print("[!] You have the wrong discord.py version! It has to be 1.0.0a ~ Exiting...")
	sys.exit(0)

from discord.ext import commands

try:
	import colorama
except ImportError:
	# Too lazy to repeat the whole process just like importing discord ^ :p
	print("[!] You don't have colorama installed!")
	print("[/] Please do 'pip3 install colorama' in order to have color! (Might not work in bash) Exiting...")
	sys.exit(0)
from colorama import Fore as F
from colorama import Style
from os import listdir
from os.path import isfile, join

# Change to True if you would like to auto-update
# NOTE: It might break your bot if I pushed a bug or made a mistake :P
auto_update = False

# To allow windows users to see colors
colorama.init(convert=True, autoreset=True)

# MAKE SURE TO MAKE YOUR OWN TOKEN.TXT 
# Opens token.txt to extract TOKEN
with open("token.txt") as f:
	char0 = f.readlines()
	TOKEN = char0[0].strip()
	f.close()

# Checks if TOKEN is valid, if not, exits
if TOKEN[0] != "N":
	print(f"{F.RED}[!] Unable to launch - No Token\nExiting...")
	sys.exit(0)

cogs = []

# Finds current path and finds all files in cogs directory
mypath = str(os.path.dirname(os.path.abspath(__file__))) + "/cogs"
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
""".format(F.BLUE,F.LIGHTYELLOW_EX)
	print(msg)
	print("~ A discord cogs package manager :)\n")
	print(f"[!] Running version: {discord.__version__}")
	# Pretty messy but gets the job done
	print(f"[!] Status: {F.GREEN}Online!")
	print(f"[/] Signed in as: {F.YELLOW}{bot.user}") 
	print(f"[/] Servers Connected: {F.MAGENTA}{len(bot.guilds)}\n")
	# Starts initializing cogs
	if not cogs:
		print(f"{F.RED}[>] No cogs available, skipping cog initialization...")
	else:
		print(f"{Style.DIM}[~] Initializing cogs...")
		for cog in cogs:
			try:
				bot.load_extension(cog)
				print(f"{F.GREEN}[*] Successfully loaded {F.YELLOW}{cog}")
			except Exception as e:
				print(f"{F.RED}[*] Unable to load {F.YELLOW}{cog}{F.WHITE}: {e}")
		print(f"[~] Finished loading cogs!\n[/] Switched to monitoring mode...have a nice day!\n")

# On launch, auto-updates
if __name__ == "__main__":
	if auto_update == True:
		print(f"{F.GREEN}[*] Auto updating..")
		try:
			os.system("git pull")
		except Exception as e:
			print(f"{F.RED}Unable to update -> {e}")
		print(f"{F.GREEN}[/] Done!")
	else:
		print(f"{F.RED}[!] Auto-update is currently off...")
		print(f"{F.MAGENTA}[>] Skipping auto-update...")
		print(f"[/] If you would like to enable auto-update, please change the auto-update variable to True")

# Command to shutdown bot cleanly
@bot.command()
async def shutdown(ctx):
	# Checks if users ID is in dev list
	if ctx.author.id not in dev:
		return await ctx.send("Hol'up, you ain't a dev")
	await ctx.send("Shutting down...")
	await bot.logout()

bot.run(TOKEN)

import discord
from discord.ext import commands
import json
import sys
import colorama
from colorama import Fore, Style
import os
from os import listdir
from os.path import isfile, join

colorama.init(convert=True, autoreset=True)

with open("token.txt") as f:
	char0 = f.readlines()
	TOKEN = char0[0]
	f.close()

if TOKEN[0] != "N":
	print(f"{Fore.RED}[!] Unable to launch - No Token\nExiting...")
	sys.exit(0)

cogs = []

mypath = os.path.dirname(os.path.abspath(__file__)) + "\cogs"
cogpath = [f for f in listdir(mypath) if isfile(join(mypath, f))]

for file in cogpath:
	cogs.append("cogs."+cogpath)

dev = [354693078495264778]

bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
	msg = """
{}__________________________________
|/////////////////////////////////|
{}|       Welcome To Bundle!        |
|/////////////////////////////////|
***********************************
""".format(Fore.BLUE,Fore.LIGHTYELLOW_EX)
	print(msg)
	print("~ A discord cogs package manager :)\n")
	print(f"[!] Status: {Fore.GREEN}Online!")
	print(f"[/] Signed in as: {Fore.YELLOW}{bot.user}") 
	print(f"[/] Servers Connected: {Fore.MAGENTA}{len(bot.guilds)}\n")

@bot.command()
async def shutdown(ctx):
	if ctx.author.id not in dev:
		return await ctx.send("Hol'up, you ain't a dev")
	await ctx.send("Shutting down...")
	await bot.logout()

if __name__ == "__main__":
	if not cogs:
		print(f"{Fore.RED}[>] No cogs available, skipping cog initialization...")
	else:
		print(f"{Style.DIM}[~] Initializing cogs...")
		for cog in cogs:
			try:
				bot.load_extension(cog)
				print(f"{Fore.GREEN}[*] Successfully loaded {cog}")
			except Exception as e:
				print(f"{Fore.RED}[*] Unable to load {Fore.WHITE}{cog}: {e}")
		print(f"[~] Finished loading cogs!\n[/] Switched to monitoring mode...have a nice day!")

bot.run(TOKEN)

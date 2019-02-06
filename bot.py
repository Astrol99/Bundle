import discord
from discord.ext import commands
import json
import sys

with open("token.txt") as f:
	char0 = f.readlines()
	TOKEN = char0[0]
	f.close()

if TOKEN[0] != "N":
	print("[!] Unable to launch - No Token\nExiting...")
	sys.exit(0)

cogs = []
dev = [354693078495264778]

bot = commands.Bot(command_prefix="./")

@bot.event
async def on_ready():
	msg = f"""
__________________________________
|/////////////////////////////////|
|       Welcome To Bundle!        |
|/////////////////////////////////|
|_________________________________|
~ A discord cogs package manager :)

[!] Status: Online!
[/] Signed in as: {bot.user} 
[/] Servers Connected: {len(bot.guilds)}
"""
	print(msg)

@bot.command()
async def shutdown(ctx):
	if ctx.author.id not in dev:
		return await ctx.send("Hol'up, you ain't a dev")
	await ctx.send("Shutting down...")
	await bot.logout()

if __name__ == "__main__":
	if not cogs:
		print("[>] No cogs available, skipping cog initialization...")
	else:
		print("[~] Initializing cogs...")
		for cog in cogs:
			try:
				bot.load_extension(cog)
				print("[*] Successfully loaded {cog}")
			except Exception as e:
				print(f"[*] Unable to load {cog}: {e}")
		print("[~] Finished loading cogs!\n[/] Switched to monitoring mode...have a nice day!")

bot.run(TOKEN)

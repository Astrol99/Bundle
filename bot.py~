import discord
from discord.ext import commands
import json


TOKEN = "NTQyNDg2Nzk5NDkxMTM3NTUw.Dzuttw.FzKIIAP6Xg_clgnWw7Q95KEbcRM"

cogs = []

bot = commands.Bot(command_prefix="bundle")

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
[~] Initializing cogs...
"""
	print(msg)

if __name__ == "__main__":
	for cog in cogs:
		try:
			bot.load_extension(cog)
			print("[*] Successfully loaded {cog}")
		except Exception as e:
			print(f"[*] Unable to load {cog}: {e}")
	print("[~] Finished loading cogs!\n[/] Switched to monitoring mode...have a nice day!")

bot.run(TOKEN)
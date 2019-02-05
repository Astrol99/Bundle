import discord
from discord.ext import commands
import json


TOKEN = ""

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
"""
	print(msg)

bot.run(TOKEN)
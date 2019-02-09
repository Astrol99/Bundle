import discord
from discord.ext import commands

class Package:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Package(bot))
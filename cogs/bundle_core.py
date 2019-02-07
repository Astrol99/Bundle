import discord
from discord.ext import commands
import os

"""
DO NOT DELETE THIS FILE AS THIS IS THE MAIN FILE
TO INSTALL PACKAGES AND REMOVE PACKAGES
"""

class Core:
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Core(bot))
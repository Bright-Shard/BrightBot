"""
Administrator/moderator commands for BrightBot
"""
# Discord.py module
import discord
# For slash commands
from discord.app_commands import command, describe
# This doesn't even need a comment, it's literally asyncio
import asyncio


class AdminCommands:
    def __init__(self, bot):
        # Store the parent bot
        self.bot = bot
        print('Admin commands loaded!')


def setup(bot: discord.Client):
    print('Loading Admin commands...')
    AdminCommands(bot)

# Discord.py library for the discord bot
import discord
# For slash commands
from discord import app_commands
# (Cogs = files with the bot commands in them)
from os import getenv
from os.path import isfile
# Twitter API access
from twitter import Api as twitterApi
# Commands for the bot
from brightbot import modules


# BrightBot, a Discord bot by BrightShard
class BrightBot(discord.Client):
    def __init__(self):
        # Environment variables
        # If the bot isn't running on Replit, load the env files from the .env file
        if isfile('.env'):
            # Import the .env library
            from dotenv import load_dotenv
            load_dotenv()

        # Set up the intents (What the bot can access)
        intents = discord.Intents.default()
        intents.members = True
        intents.message_content = True

        # Set up the bot
        super().__init__(intents=intents)

        # Set up the Twitter API
        # In order, the tokens are: Access token, access secret, API key, API secret
        self.twitter = twitterApi(
            access_token_key=getenv('ATOKEN'),
            access_token_secret=getenv('ASECRET'),
            consumer_key=getenv('CKEY'),
            consumer_secret=getenv('CSEC'))

        # The command tree
        self.commands = app_commands.CommandTree(self)

        # Import the other commands
        for module in modules:
            module.setup(self)

        # On ready
        @self.event
        async def on_ready():
            # The loaded bot commands
            loadedCommands = self.commands.get_commands()
            # Show that the bot is logged in
            print(f"------\n|-Logged in as: {self.user.name}\n------\n|-Commands loaded: ")
            for command in loadedCommands:
                print(f"  |-{command.name}")
            print('------')

        # Command to sync the bot commands
        @self.event
        async def on_message(message) -> None:
            if message.author == self.user:
                return

            if message.content.startswith('brightbot-update'):
                try:
                    await self.commands.sync(guild=message.guild)
                    await message.channel.send('Commands updated.')
                except discord.errors.Forbidden:
                    await message.channel.send('There was an error syncing. :(')


BrightBot().run(getenv('TOKEN'))

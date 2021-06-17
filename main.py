# BrightBot, made by BrightShard
# This code is open-source on GitHub: https://github.com/Bright-Shard/BrightBot

import discord # Discord modules for making the bot
from discord.ext import commands # Discord modules for making the bot
import os # Get Replit secrets
from replit import db # Store data in the DB

botIntents = discord.Intents.default() # Set up the bot's intents
botIntents.members = True # Set up the bot's intents
bot = commands.Bot(command_prefix=">",intents=botIntents) # Load the bot
bot.remove_command('help') # Remove help command so we can insert our own

# Load cogs dynamically 
if __name__ == '__main__':
    for cog in os.listdir('cogs'):
        splitName = cog.split('.')
        if splitName[len(splitName) - 1] == 'py':
            print(f'Loading cog: {splitName[0]}.py')
            bot.load_extension(f'cogs.{splitName[0]}')

@bot.event # Show the bot is loaded
async def on_ready():
    print('------')
    print('Logged in as:')
    print(bot.user.name)
    print('------')
    print('Commands loaded:')
    print([x.name for x in bot.commands])

bot.run(os.getenv('TOKEN')) # Launch the bot
# loadWebServer() # Launch the web server
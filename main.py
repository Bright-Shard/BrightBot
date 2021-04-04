# BrightBot, made by BrightShard
# This code is open-source on GitHub: https://github.com/Bright-Shard/BrightBot

import discord, os # Import discord.py for making the bot and os for getting environment variables
from discord.ext import commands, tasks # Import the commands sublibrary to make the bot and tasks sublibrary for background processes
from server import keep_alive # This is the web server, used to keep the bot online so Replit doesn't shut it down
import asyncio # Used for timed delays
import random # Used to pick random numbers
import twitter # Used for getting twitter stuff
import adminCommands, userCommands, betaCommands # Import commands because they are in separate files

# Twitter API for getting tweets
twit = twitter.Twitter(auth=twitter.OAuth(
  os.getenv('ATOKEN'), # Set environment variable ATOKEN to your access token
  os.getenv('ASECRET'), # Set environment variable ASECRET to your access secret
  os.getenv('CKEY'), # Set environment variable CKEY to your API key
  os.getenv('CSEC'))) # Set environment variable CSEC to your API secret

botIntents = discord.Intents.default() # Declare the bot's intents, AKA what permissions it has as a Discord bot
botIntents.members = True

bot = commands.Bot(command_prefix=".",intents=botIntents) # Load the bot
bot.remove_command('help') # Remove help command so we can insert our own

global GMCTweets # Get tweets from Giant Military Cats' twitter
GMCTweets = twit.statuses.user_timeline(screen_name='giantcat9',count=30)
@tasks.loop(hours=12.0)
async def getTwitter():
  global GMCTweets
  GMCTweets = twit.statuses.user_timeline(screen_name='giantcat9',count=30)

@bot.command(name='help',brief='The help command. Run help <command> for help on a specific command.',description='Run .help to see the list of commands, or .help <command> for info on a specific command.',aliases=['Help','HELP'])
async def help(ctx, *section: str):
  try:
    if section[0] == 'admin':
      msg = discord.Embed(description="Here's the list of admin commands. All commands start with `.` and can be capitilized or lowercase. Also, you can run `.help <command_name>` for more info on a command. \n NOTE: You need the `admin_commands` role to run these commands.")
      msg.set_author(name="BrightBot Admin Commands")
      for command in bot.commands:
        try: # Help command has no cog, so add a try/except command to pass over it without error
          if command.cog.qualified_name == "Admin Commands":
            msg.add_field(name=command.name,value=command.brief)
        except:
          pass
      await ctx.send(embed=msg)
    elif section[0] == 'user':
      msg = discord.Embed(description="Here's the list of commands anyone can run. They start with `.` and can be capitilized or lowercase. You can run `.help <command_name>` for more info on a command.")
      msg.set_author(name="BrightBot Commands")
      for command in bot.commands:
        try:
          if command.cog.qualified_name == "User Commands":
            msg.add_field(name=command.name,value=command.brief)
        except:
          pass
      await ctx.send(embed=msg)
    elif section[0] != ' ':
      try:
        cmd = bot.get_command(section[0])
        msg = discord.Embed(description=cmd.description)
        msg.set_author(name=str("." + cmd.name + " Command"))
        await ctx.send(embed=msg)
      except:
        msg = discord.Embed(description="Error: Unknown command to get help for. \n Please run `.help user` for user commands, `.help admin` for admin commands, or `.help <command_name>` for info on a specific command.")
        msg.set_author(name="BrightBot Help")
        await ctx.send(embed=msg)
  except:
    msg = discord.Embed(description='Please run `.help user` for user commands, `.help admin` for admin commands, or `.help <command_name>` for info on a specific command.')
    msg.set_author(name="BrightBot Help")
    await ctx.send(embed=msg)

bot.add_cog(adminCommands.admin(bot)) # Import the command cogs
bot.add_cog(userCommands.user(bot))
bot.add_cog(betaCommands.beta(bot))

@bot.event # Print who the bot is logged in as when it starts
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print('------')

keep_alive()
bot.run(os.getenv('TOKEN'))

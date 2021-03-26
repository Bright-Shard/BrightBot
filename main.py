# BrightBot, made by BrightShard
# This code is open-source on GitHub: https://github.com/Bright-Shard/BrightBot

import discord, os # Import discord.py for making the bot and os for getting environment variables
from discord.ext import commands, tasks # Import the commands sublibrary to make the bot and tasks sublibrary for background processes
from server import keep_alive # This is the web server, used to keep the bot online so Replit doesn't shut it down
import asyncio # Used for timed delays
import random # Used to pick random numbers
import twitter # Used for getting twitter stuff
import json # For parsing JSON files like memes
import requests # For getting remote content

# Twitter API for getting tweets
twit = twitter.Twitter(auth=twitter.OAuth(
  os.getenv('ATOKEN'), # Set environment variable ATOKEN to your access token
  os.getenv('ASECRET'), # Set environment variable ASECRET to your access secret
  os.getenv('CKEY'), # Set environment variable CKEY to your API key
  os.getenv('CSEC'))) # Set environment variable CSEC to your API secret

botIntents = discord.Intents.default() # Declare the bot's intents, AKA what permissions it has as a Discord bot
botIntents.members = True

bot = commands.Bot(command_prefix=".",intents=botIntents) # Load the bot with the command prefix "."

global GMCTweets
GMCTweets = twit.statuses.user_timeline(screen_name='giantcat9',count=30)

@tasks.loop(hours=12.0)
async def getTwitter():
  global GMCTweets
  GMCTweets = twit.statuses.user_timeline(screen_name='giantcat9',count=30)

@bot.event # Print who the bot is logged in as when it starts
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print('------')

# The addRole command, used to add a role to a user
@bot.command(name='addRole',brief='Add a role to a user. Needs admin_commands role.',description='Add a role to someone on the server. You can add multiple roles or just one. You can ping the person and role or just type their names. Needs admin_commands role.',aliases=['addrole','AddRole','Addrole','arole']) # Declare it as a command, set it's brief description, long description, and command aliases
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def addRole(ctx, user: discord.Member, *roles: discord.Role): # Then make a function to handle the command
  await ctx.send(f'Giving user {user.name} the roles {[i.name for i in roles]}.') # Sends in the chat who is getting what roles
  for role in roles: # Iterate through the roles received from the command and add them to the given user
    await user.add_roles(role)

# The removeRole command, used to remove a user's role
@bot.command(name='removeRole',brief='Remove a role froma user. Needs admin_commands role.',description='Remove a role from someone on the server. You can remove multiple roles or just one. You can ping the person and role or just type their names. Needs admin_commands role.') # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def removeRole(ctx, user: discord.Member, *roles: discord.Role):
  await ctx.send(f'Removing the roles {[i.name for i in roles]} from user {user.name}.')
  for role in roles:
    await user.remove_roles(role)

@bot.command(name='purge',brief='Cleanse the chat. Of messages. Needs admin_commands role.',description='Deletes a TON of messages.',aliases=['PURGE']) # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def purge(ctx):
  await ctx.send('Purging the chat in 5...')
  await asyncio.sleep(1)
  await ctx.send('Purging the chat in 4...')
  await asyncio.sleep(1)
  await ctx.send('Purging the chat in 3...')
  await asyncio.sleep(1)
  await ctx.send('Purging the chat in 2...')
  await asyncio.sleep(1)
  await ctx.send('Purging the chat in 1...')
  await asyncio.sleep(1)
  await ctx.send('ThE PuRGe iS hERE.')
  await asyncio.sleep(1)
  await ctx.channel.purge()

@bot.command(name='mute',brief='Mute someone. Requires the admin_commands role.',description='Adds a Muted role to whoever is mentioned. You can ping them or just type their username.',aliases=['Mute']) # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def mute(ctx, user: discord.Member):
  await ctx.send(f'Muting {user.name}.')
  await user.add_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

@bot.command(name='unmute',brief='Unmute someone. Requires the admin_commands role.',description='Removes the Muted role from whoever is mentioned. You can ping them or just type their username.',aliases=['Unmute','unMute','UnMute']) # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def unmute(ctx, user: discord.Member):
  await ctx.send(f'Unmuting {user.name}')
  await user.remove_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

@bot.command(name='ban',brief='Ban someone from the server. Needs the admin_commands role.',description='Bans whoever is mentioned. You can ping them or just type their name.',aliases=['Ban','banhammer','BanHammer','banHammer','Banhammer','hammer','Hammer','HAMMER']) # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def ban(ctx, user: discord.Member, *banReason: str):
  await ctx.send(f'{user.name} was HAMMERED by {ctx.author}, RIP.')
  finalReason = str(banReason)
  finalReason += '(Banned by ' + str({ctx.author}) + ')'
  await user.ban(reason=finalReason)

@bot.command(name='kick',brief='Kick someone from the server. Needs the admin_commands role.',description='Kicks the person named in this command. You can ping them or just type out their username.',aliases=['Kick','remove','Remove']) # Same as above
@commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
async def kick(ctx, user: discord.Member, *kickReason: str):
  await ctx.send(f'{ctx.author} decided {user.name} could no longer be with us.')
  finalReason = str(kickReason) + '(Kicked by ' + str({ctx.author}) + ')'
  await user.kick(reason=finalReason)

@bot.command(name='meme',brief='Gets a random meme from teh interwebz.',description='Gets a meme from https://meme-api.herokuapp.com/gimme, then sends it in the chat.',aliases=['Meme'])
async def meme(ctx):
  content = requests.get('https://meme-api.herokuapp.com/gimme')
  refinedContent = json.loads(content.text)
  msg = discord.Embed(title=refinedContent['title'])
  msg.set_image(url=refinedContent['url'])
  await ctx.send(embed=msg)

@bot.command(name='GMC',brief='Gets a random tweet from Giant Military Cats.',description='Uses nitter.net and RSS to get a random tweet from Giant Military Cats (https://twitter.com/giantcat9).',aliases=['gmc','cat','giantcat'])
async def GMC(ctx):
  try:
    tweet = GMCTweets[random.randint(0,29)]
    text = tweet['text'] + '\n Source: https://twitter.com/giantcat9'
    img = tweet['entities']['media'][0]['media_url_https']
    msg = discord.Embed(title='Giant Military Cats',link='https://twitter.com/giantcat9',description=text)
    msg.set_image(url=img)
    await ctx.send(embed=msg)
  except:
    await GMC(ctx=ctx)

keep_alive()
bot.run(os.getenv('TOKEN'))
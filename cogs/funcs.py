'''
Funcs.py - a few helpful functions used in BrightBot
'''

# Imports
from replit import db, web
import discord
from discord.ext import tasks
import twitter
import os

# Web server, to keep bot online 24/7
def loadWebServer():
    app = web.App("BrightBot")

    @app.route('/')
    def index():
        return "I'm a Discord bot. You can invite me to your server <a href='https://discord.com/api/oauth2/authorize?client_id=745433967486042133&permissions=8&scope=bot'>here!</a>"


# Twitter API for getting tweets
# In order, the tokens are: Access token, access secret, API key, API secret
twit = twitter.Api(
  access_token_key=os.getenv('ATOKEN'),
  access_token_secret=os.getenv('ASECRET'),
  consumer_key=os.getenv('CKEY'),
  consumer_secret=os.getenv('CSEC'))

# Tweets from Giant Military Cats
GMCTweets = twit.GetUserTimeline(screen_name='giantcat9',count=30)
@tasks.loop(hours=12.0)
async def getTwitter():
  global GMCTweets
  GMCTweets = twit.GetUserTimeline(screen_name='giantcat9',count=30)

# Check for proper roles
async def role_checker(ctx, role):
    targetRoleList = [x.name for x in ctx.author.roles]
    if str(role) in targetRoleList:
      return True
    else:
      await ctx.send(f"You need the `{str(role)}` role to run this command.")
      return False

def setup(bot):
    pass
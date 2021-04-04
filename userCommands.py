'''
User Commands:
These commands can be run by anyone on the server. Right now I only have 2 meme commands:
- meme: Gets a random meme from a meme API (https://meme-api.herokuapp.com/gimme) and displays it in the server.
- gmc: Gets a random tweet from Giant Military Cats (https://twitter.com/giantcat9) and displays it in the server.

The file uses the discord.py library for commands and command cogs; uses the os library to get environment variables, like API keys; the requests library to query the meme API; the json library to parse the returned memes; and the random library to pick a random tweet from Giant Military Cats.
'''

import discord, os, requests, json, random
from discord.ext import commands

class user(commands.Cog, name="User Commands"):
  @commands.command(name='meme',brief='Gets a random meme from teh interwebz.',description='Gets a meme from [an API](https://meme-api.herokuapp.com/gimme), then sends it in the chat.',aliases=['Meme'])
  async def meme(ctx):
    content = requests.get('https://meme-api.herokuapp.com/gimme')
    refinedContent = json.loads(content.text)
    msg = discord.Embed(title=refinedContent['title'])
    msg.set_image(url=refinedContent['url'])
    await ctx.send(embed=msg)

  @commands.command(name='GMC',brief='Gets a random tweet from Giant Military Cats.',description='Uses twitter to get a random tweet from [Giant Military Cats](https://twitter.com/giantcat9).',aliases=['gmc','cat','giantcat'])
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

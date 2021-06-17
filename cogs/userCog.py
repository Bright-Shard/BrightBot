'''
User Commands:
These commands can be run by anyone on the server.
'''

import discord
import requests
import json
import random
from discord.ext import commands
from cogs.funcs import GMCTweets


class user(commands.Cog, name="User Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='meme',brief='Gets a random meme from teh interwebz.',description='`>meme`: Gets a meme from [an API](https://meme-api.herokuapp.com/gimme), then sends it in the chat.',aliases=['Meme'])
    async def meme(self, ctx):
        content = requests.get('https://meme-api.herokuapp.com/gimme')
        refinedContent = json.loads(content.text)
        msg = discord.Embed(title=refinedContent['title'])
        msg.set_image(url=refinedContent['url'])
        await ctx.send(embed=msg)

    @commands.command(name='GMC',brief='Gets a random tweet from Giant Military Cats.',description='`>meme`: Uses twitter to get a random tweet from [Giant Military Cats](https://twitter.com/giantcat9).',aliases=['gmc','cat','giantcat'])
    async def GMC(self, ctx):
        try:
            tweet = GMCTweets[random.randint(0,29)]
            text = tweet['text'] + '\n Source: https://twitter.com/giantcat9'
            img = tweet['entities']['media'][0]['media_url_https']
            msg = discord.Embed(title='Giant Military Cats',link='https://twitter.com/giantcat9',description=text)
            msg.set_image(url=img)
            await ctx.send(embed=msg)
        except:
            await self.GMC(ctx=ctx)

def setup(bot):
    bot.add_cog(user(bot))
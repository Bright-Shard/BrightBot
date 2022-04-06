"""
General commands for BrightBot
"""
# Discord.py module
import discord
from discord.app_commands import command
# For APIs
from json import loads as loadJSON
from requests import get as request
# For fun
from random import choice as random
from random import randint as randomNumber
# For background tasks
from discord.ext import tasks


class UserCommands:
    def __init__(self, bot):
        # Store the parent bot
        self.bot = bot
        # For getting tweets
        self.twitter = bot.twitter
        # Giant Military Cats tweets
        self.gmcTweets = self.twitter.GetUserTimeline(screen_name='giantcat9', count=30)
        # Science Diagrams that Look Like Shitposts tweets
        self.scienceTweets = self.twitter.GetUserTimeline(screen_name='scienceshitpost', count=30)
        # Add the commands to the bot
        self.bot.commands.add_command(self.ping)
        self.bot.commands.add_command(self.getMeme)
        self.bot.commands.add_command(self.gmcTwitter)
        self.bot.commands.add_command(self.scienceDiagramsTwitter)
        print('User commands loaded!')

    @command(name='ping')
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message('Pong!')

    @command(name='meme')
    async def getMeme(self, interaction: discord.Interaction):
        meme = loadJSON(request('https://meme-api.herokuapp.com/gimme').text)
        embed = discord.Embed(title=meme['title'])
        embed.set_image(url=meme['url'])
        await interaction.response.send_message(embed=embed)

    @command(name='gmc')
    async def gmcTwitter(self, interaction: discord.Interaction):
        tweet = self.gmcTweets[randomNumber(0, 29)].AsDict()
        embed = discord.Embed(title=random(['Haha cat go brrrr', 'Cat superiority', '<3 cats']),
                              link='https://twitter.com/giantcat9',
                              description=f"{tweet['text']}\nSee more: https://twitter.com/giantcat9")
        try:
            embed.set_image(url=tweet['media'][0]['media_url_https'])
        except KeyError:
            await self.gmcTwitter(interaction)
        await interaction.response.send_message(embed=embed)

    @command(name='skience')
    async def scienceDiagramsTwitter(self, interaction: discord.Interaction):
        tweet = self.scienceTweets[randomNumber(0, 29)].AsDict()
        embed = discord.Embed(title=random(['I N T E L L I G E N C E', 'Smert', 'Biggus Brainus']),
                              link='https://twitter.com/giantcat9',
                              description=f"{tweet['text']}\nSee more: https://twitter.com/giantcat9")
        try:
            embed.set_image(url=tweet['media'][0]['media_url_https'])
        except KeyError:
            await self.scienceDiagramsTwitter(interaction)
        await interaction.response.send_message(embed=embed)

    @tasks.loop(hours=12.0)
    async def refreshTweets(self):
        # Giant Military Cats tweets
        self.gmcTweets = self.twitter.GetUserTimeline(screen_name='giantcat9', count=30)
        # Science Diagrams that Look Like Shitposts tweets
        self.scienceTweets = self.twitter.GetUserTimeline(screen_name='scienceshitpost', count=30)


def setup(bot):
    print('Loading User commands...')
    UserCommands(bot)

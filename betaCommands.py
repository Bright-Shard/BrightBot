'''
Beta Commands:
These are commands that are being tested or have not been finished.
'''
import discord, os
from discord.ext import commands

class beta(commands.Cog,name="Beta Commands"):
  @commands.command(name='msgRole',brief='Adds reaction roles to a message.',description='Adds spcified roles to people who use certain reactions on the specified message.',aliases=['messageRole','MessageRole','MsgRole','MSGRole'])
  async def msgRole(ctx, channel, message):
    async def addMsgRole():
      await ctx.send('React with the emoji you want to give a role.')
      await ctx.send('Name the role you want that emoji to give.')
      await ctx.send('Saved! Do you want to add another reaction role?')

    defEmojiMsg = await ctx.send('React with the emoji you want to give a role.')
    emojiMsgCtx = await bot.get_context(defEmojiMsg)
    emojiMsg = emojiMsgCtx.message
    @bot.listen('on_reaction_add')
    async def defEmoji(emoji, sender):
      if sender.id != bot.user.id:
        if reaction.message == msg:
          emoji = reaction.emoji
    await ctx.send('Name the role you want that emoji to give. (Type it\'s name, don\'t ping it.)')
    @bot.listen('on_message')
    async def defRole(msg):
      if msg.guild == ctx.guild:
        if msg.channel == ctx.channel:
          if msg.author == ctx.author:
            \
    await ctx.send('Saved! Do you want to add another reaction role?')

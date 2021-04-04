'''
Admin Commands:
These commands can only be run by users in the server that have the admin_commands role. These are the current commands:
- addRole: Gives someone a role
- removeRole: Removes a role from someone
- purge: Deletes a ton of messages from the chat
- mute: Gives someone the Muted role, you will need to set which channel that role can't type in
- unmute: Removes the Muted role from someone
- ban: Bans a member
- kick: Kicks a member

This script uses the discord.py library for commands and command cogs.
'''
import discord, os
from discord.ext import commands

class admin(commands.Cog, name="Admin Commands"):
  # The addRole command, used to add a role to a user
  @commands.command(name='addRole',brief='Add a role to a user.',description='`.addRole <person> <role(s)>`: Adds <role(s)> to <person>. You can list multiple roles, hence the (s) on the end.',aliases=['addrole','AddRole','Addrole','arole']) # Declare it as a command, set it's brief description, long description, and command aliases
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def addRole(self, ctx, user: discord.Member, *roles: discord.Role): # Then make a function to handle the command
    await ctx.send(f'Giving user {user.name} the roles {[i.name for i in roles]}.') # Sends in the chat who is getting what roles
    for role in roles: # Iterate through the roles received from the command and add them to the given user
      await user.add_roles(role)

  # The removeRole command, used to remove a user's role
  @commands.command(name='removeRole',brief='Remove a role froma user.',description='`.removeRole <person> <role(s)>`: Removes <role(s)> from <person>. You can list multiple roles, hence the (s) at the end.',aliases=['removerole','RemoveRole','.Removerole','rrole']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def removeRole(self, ctx, user: discord.Member, *roles: discord.Role):
    await ctx.send(f'Removing the roles {[i.name for i in roles]} from user {user.name}.')
    for role in roles:
      await user.remove_roles(role)

  @commands.command(name='purge',brief='Cleanse the chat. Of messages.',description='`.purge`: No arguments. Cleanses the chat of messages.',aliases=['PURGE']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def purge(self, ctx):
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

  @commands.command(name='mute',brief='Mute someone.',description='`.mute <person>`: Adds the `Muted` role to <person>. You will have to manually add the `Muted` role and set which channels it can\'t talk in.',aliases=['Mute']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def mute(self, ctx, user: discord.Member):
    await ctx.send(f'Muting {user.name}.')
    await user.add_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

  @commands.command(name='unmute',brief='Unmute someone.',description='`.unmute <person>`: Removes the `Muted` role from <person>.',aliases=['Unmute','unMute','UnMute']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def unmute(self, ctx, user: discord.Member):
    await ctx.send(f'Unmuting {user.name}')
    await user.remove_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

  @commands.command(name='ban',brief='Ban someone from the server.',description='`.ban <person> [reason]`: Bans <person>. If a [reason] is provided, I will DM <person> with the provided [reason].',aliases=['Ban','banhammer','BanHammer','banHammer','Banhammer','hammer','Hammer','HAMMER']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def ban(self, ctx, user: discord.Member, *banReason: str):
    await ctx.send(f'{user.name} was HAMMERED by {ctx.author}, RIP.')
    reason = ''
    for i in banReason:
      reason += i
      reason += " "
    await user.ban(reason=str(reason + f" (Banned by {ctx.author})"))
    msg = discord.Embed(title=f"You were banned from {ctx.guild}!",description=f"You were banned by {ctx.author}. \n Their reason was: {reason}")
    await user.send(embed=msg)

  @commands.command(name='kick',brief='Kick someone from the server.',description='`.kick <person> [reason]`: Kicks <person>. If a [reason] is provided, I will DM <person> with the provided [reason].',aliases=['Kick','remove','Remove']) # Same as above
  @commands.has_role('admin_commands') # Make sure whoever is running the command has the admin_commands role
  async def kick(self, ctx, user: discord.Member, *kickReason: str):
    await ctx.send(f'{ctx.author} decided {user.name} could no longer be with us.')
    reason = ''
    for i in kickReason:
      reason += i
      reason += " "
    await user.kick(reason=str(reason + f" (Kicked by {ctx.author})"))
    msg = discord.Embed(title=f"You were kicked from {ctx.guild}!",description=f"You were kicked by {ctx.author}. \n Their reason was: {reason}")
    await user.send(embed=msg)

import discord, os
from discord.ext import commands
from server import keep_alive
import asyncio

botIntents = discord.Intents.default()
botIntents.members = True

bot = commands.Bot(command_prefix=".",intents=botIntents)

@bot.event
async def on_ready():
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(name='addRole',brief='Add a role to a user. Needs admin_commands role.',description='Add a role to someone on the server. You can add multiple roles or just one. You can ping the person and role or just type their names. Needs admin_commands role.',aliases=['addrole','AddRole','Addrole','arole'])
@commands.has_role('admin_commands')
async def addRole(ctx, user: discord.Member, *roles: discord.Role):
  await ctx.send(f'Giving user {user.name} the roles {[i.name for i in roles]}.')
  for role in roles:
    await user.add_roles(role)

@bot.command(name='removeRole',brief='Remove a role froma user. Needs admin_commands role.',description='Remove a role from someone on the server. You can remove multiple roles or just one. You can ping the person and role or just type their names. Needs admin_commands role.')
@commands.has_role('admin_commands')
async def removeRole(ctx, user: discord.Member, *roles: discord.Role):
  await ctx.send(f'Removing the roles {[i.name for i in roles]} from user {user.name}.')
  for role in roles:
    await user.remove_roles(role)

@bot.command(name='purge',brief='Cleanse the chat. Of messages. Needs admin_commands role.',description='Deletes a TON of messages.',aliases=['PURGE'])
@commands.has_role('admin_commands')
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

@bot.command(name='mute',brief='Mute someone. Requires the admin_commands role.',description='Adds a Muted role to whoever is mentioned. You can ping them or just type their username.',aliases=['Mute'])
@commands.has_role('admin_commands')
async def mute(ctx, user: discord.Member):
  await ctx.send(f'Muting {user.name}.')
  await user.add_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

@bot.command(name='unmute',brief='Unmute someone. Requires the admin_commands role.',description='Removes the Muted role from whoever is mentioned. You can ping them or just type their username.',aliases=['Unmute','unMute','UnMute'])
@commands.has_role('admin_commands')
async def unmute(ctx, user: discord.Member):
  await ctx.send(f'Unmuting {user.name}')
  await user.remove_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

@bot.command(name='ban',brief='Ban someone from the server. Needs the admin_commands role.',description='Bans whoever is mentioned. You can ping them or just type their name.',aliases=['Ban','banhammer','BanHammer','banHammer','Banhammer','hammer','Hammer','HAMMER'])
@commands.has_role('admin_commands')
async def ban(ctx, user: discord.Member, *banReason: str):
  finalReason = ''
  for i in banReason:
    finalReason += i
  finalReason += '\n Banned by '
  finalReason += {ctx.author}
  await user.ban(reason=finalReason)
  await ctx.send(f'{user.name} was HAMMERED by {ctx.author}, RIP.')

keep_alive()
bot.run(os.getenv('TOKEN'))
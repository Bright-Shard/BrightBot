'''
Admin Commands:
Commands that can only be used by users with the `admin_commands` role.
'''
import discord
from discord.ext import commands
import asyncio
from cogs.funcs import role_checker


class admin(commands.Cog, name="Admin Commands"):
    def __init__(self, bot):
        self.bot = bot

    async def has_admin_role(ctx):
        check = await role_checker(ctx, 'admin_commands')
        return check
    
    # AddRole command: Add a role to a user without having to open settings.
    @commands.command(name='addRole',brief='Add a role to a user.',description='`>addRole <person> <role(s)>`: Adds <role(s)> to <person>. You can list multiple roles.',aliases=['addrole','AddRole','Addrole','arole'])
    @commands.check(has_admin_role)
    async def addRole(self, ctx, user: discord.Member, *roles: discord.Role):
        await ctx.send(f'Giving user {user.name} the roles {[i.name for i in roles]}.')
        for role in roles:
            await user.add_roles(role)

    # RemoveRole command: Remove a role from a user without having to open settings.
    @commands.command(name='removeRole',brief='Remove a role froma user.',description='`>removeRole <person> <role(s)>`: Removes <role(s)> from <person>. You can list multiple roles.',aliases=['removerole','RemoveRole','.Removerole','rrole'])
    @commands.check(has_admin_role)
    async def removeRole(self, ctx, user: discord.Member, *roles: discord.Role):
        await ctx.send(f'Removing the roles {[i.name for i in roles]} from user {user.name}.')
        for role in roles:
            await user.remove_roles(role)

    # Purge command: Delete a frick ton of messages from the chat. Also send a cool countdown :)
    @commands.command(name='purge',brief='Cleanse the chat. Of messages.',description='`>purge`: No arguments. Cleanses the chat of messages.',aliases=['PURGE'])
    @commands.check(has_admin_role)
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
        await ctx.send(f'Channel was purged by {ctx.author}.')

    # Mute command: Give whoever is listed the `Muted` role.
    @commands.command(name='mute',brief='Mute someone.',description='`>mute <person>`: Adds the `Muted` role to <person>. You will have to manually add the `Muted` role and set which channels it can/can\'t talk in.',aliases=['Mute'])
    @commands.check(has_admin_role)
    async def mute(self, ctx, user: discord.Member):
        await ctx.send(f'Muting {user.name}.')
        await user.add_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

    # Unmute command: Remove the `Muted` role from whoever is listed.
    @commands.command(name='unmute',brief='Unmute someone.',description='`>unmute <person>`: Removes the `Muted` role from <person>.',aliases=['Unmute','unMute','UnMute'])
    @commands.check(has_admin_role)
    async def unmute(self, ctx, user: discord.Member):
        await ctx.send(f'Unmuting {user.name}')
        await user.remove_roles(discord.utils.get(ctx.guild.roles,name='Muted'))

    # Ban command: Ban a user, and DM them a reason if a reason was provided.
    @commands.command(name='ban',brief='Ban someone from the server.',description='`>ban <person> [reason]`: Bans <person>. If a [reason] is provided, I will DM <person> with the provided [reason].',aliases=['Ban','banhammer','BanHammer','banHammer','Banhammer','hammer','Hammer','HAMMER'])
    @commands.check(has_admin_role)
    async def ban(self, ctx, user: discord.Member, *banReason: str):
        await ctx.send(f'{user.name} was HAMMERED by {ctx.author}, RIP.')
        reason = ''
        for i in banReason:
            reason += i
            reason += " "
        await user.ban(reason=str(reason + f" (Banned by {ctx.author})"))
        msg = discord.Embed(title=f"You were banned from {ctx.guild}!",description=f"You were banned by {ctx.author}. \n Their reason was: {reason}")
        await user.send(embed=msg)

    # Kick command: Kick a user, and DM them a reason if a reason was provided.
    @commands.command(name='kick',brief='Kick someone from the server.',description='`>kick <person> [reason]`: Kicks <person>. If a [reason] is provided, I will DM <person> with the provided [reason].',aliases=['Kick','remove','Remove'])
    @commands.check(has_admin_role)
    async def kick(self, ctx, user: discord.Member, *kickReason: str):
        await ctx.send(f'{ctx.author} decided {user.name} could no longer be with us.')
        reason = ''
        for i in kickReason:
            reason += i
            reason += " "
        await user.kick(reason=str(reason + f" (Kicked by {ctx.author})"))
        msg = discord.Embed(title=f"You were kicked from {ctx.guild}!",description=f"You were kicked by {ctx.author}. \n Their reason was: {reason}")
        await user.send(embed=msg)

def setup(bot):
    bot.add_cog(admin(bot))
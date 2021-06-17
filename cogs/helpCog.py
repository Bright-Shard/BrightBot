'''
Help Command:
The custom help command is really long, so I gave it it's own file. LOL.
'''

from cogs.funcs import role_checker
from discord.ext import commands
import discord

class helpCommand(commands.Cog, name='Help Command'):
    def __init__(self, bot):
        self.bot = bot
    
    # Custom help command
    @commands.command(name='help',brief='The help command. Run `>help <command>` for help on a specific command.',description='Run `>help [admin] [user]` to see the list of commands, or `>help <command>` for info on a specific command.',aliases=['Help','HELP'])
    async def help(self, ctx, section=' '):
        if section == 'admin':
            hasAdmin = await role_checker(ctx, 'admin_commands')
            if hasAdmin:
                msg = discord.Embed(description='Commands start with `>` \n Commands can be capital or lowercase \n `<>`: Required argument \n `[]`: Optional argument')
                msg.set_author(name='BrightBot Help - Admin Commands')
                for command in self.bot.commands:
                    try:
                        if command.cog.qualified_name == 'Admin Commands' or command.cog.qualified_name == 'Message Commands':
                            msg.add_field(name=command.name,value=command.brief)
                    except:
                        pass
                await ctx.send(embed=msg)
            
        elif section == 'user':
            msg = discord.Embed(description='Commands start with `>` \n Commands can be capital or lowercase \n `<>`: Required argument \n `[]`: Optional argument')
            msg.set_author(name="BrightBot Help - User Commands")
            for command in self.bot.commands:
                if command.cog.qualified_name == "User Commands":
                    msg.add_field(name=command.name,value=command.brief)
            await ctx.send(embed=msg)
                
        elif section != ' ':
            try:
                cmd = self.bot.get_command(section)
                msg = discord.Embed(description=cmd.description)
                msg.set_author(name=str("BrightBot Help - " + cmd.name + " Command"))
                await ctx.send(embed=msg)
            except:
                msg = discord.Embed(description="Error: Unknown command or section. \n Please run `>help user` for user commands, `>help admin` for admin commands, or `>help <command_name>` for info on a specific command.")
                msg.set_author(name="BrightBot Help - Error")
                await ctx.send(embed=msg)
        else:
            msg = discord.Embed(description='Please run `>help user` for user commands, `>help admin` for admin commands, or `>help <command_name>` for info on a specific command.')
            msg.set_author(name="BrightBot Help - Main")
            await ctx.send(embed=msg)

def setup(bot):
    bot.add_cog(helpCommand(bot))
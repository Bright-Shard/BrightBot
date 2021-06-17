'''
Beta Commands:
These are commands that are being tested or have not been finished.
'''
import discord
from discord.ext import commands
from replit import db
from cogs.funcs import role_checker


class message(commands.Cog,name='Message Commands'):
    def __init__(self, bot):
        self.bot = bot
        self.whatToWatch = {}

    async def has_admin_role(ctx):
        check = await role_checker(ctx, 'admin_commands')
        return check

    @commands.command(name='rulesMsg',brief='Make an embed with the rules.',description='`>rulesMsg`: Make an embed with the list of rules. There are no arguments as the command uses a setup wizard.',aliases=['RulesMessage','rulesMessage','Rulesmessage','rulesmessage','RulesMsg','Rulesmsg','rulesmsg','ruleMsg','RuleMsg','rulemsg'])
    @commands.check(has_admin_role)
    async def rulesMsg(self, ctx):
        embedDict = {'title': 'Rules','fields':[],'description': 'This rules section was made with BrightBot.'}
        sectionToNumber = {}

        def check_author(msg):
            return msg.author == ctx.author and msg.channel == ctx.channel

        async def add_section():
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - New Section Name',description='Please send the **name** of this rules section.'))
            name = await self.bot.wait_for('message',check=check_author)
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - New Section Text',description='Please send the **content** of this rules section.'))
            text = await self.bot.wait_for('message',check=check_author)
            embedDict['fields'].append({'name': name.content,'value': text.content})
            sectionToNumber[name.content] = len(embedDict['fields']) - 1
            await main_menu()

        async def edit_section():
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Edit Section Name',description='Please send the **name** of the rules section to edit.'))
            name = await self.bot.wait_for('message',check=check_author)
            try:
                embedDictFields = embedDict['fields']
                sectionToEdit = embedDictFields[sectionToNumber[name.content]]
                await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Edit Section Text',description='Please send the new **text** for the section.'))
                text = await self.bot.wait_for('message',check=check_author) 
                sectionToEdit['value'] = text.content
            except:
                await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Error',description='Unknown section name.'))
                await edit_section()
            await main_menu()
            

        async def save_rules():
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Set Title',description='Send the **title** of the whole rules message.'))
            title = await self.bot.wait_for('message',check=check_author)
            embedDict['title'] = title.content
            embed = discord.Embed.from_dict(embedDict)
            await ctx.send(embed=embed)
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Ready to Send',description='The embed above is what your rules will look like. Ready to send? Send `yes` or `no`.'))
            isReady = await self.bot.wait_for('message',check=check_author)
            if isReady.content == 'yes':
                await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Send Rules',description='Perfect! Send the **Channel ID** of the channel to upload the rules to. (Need help with this? Look up \"How to get Discord channel ID\")'))
                channelName = await self.bot.wait_for('message',check=check_author)
                try:
                    channel = self.bot.get_channel(int(channelName.content))
                    embed = discord.Embed.from_dict(embedDict)
                    await channel.send(embed=embed)
                    await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Finished',description='Rules successfully sent!'))
                except:
                    await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Error',description='Unknown channel ID.'))
                    await save_rules()
            elif isReady.content == 'no':
                main_menu()
            else:
                await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Error',description='Unknown response.'))
                await save_rules()

        async def main_menu():
            await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Main Menu',description='Say `new` to make a new Rules Section, `edit` to edit an existing Rules Section, `view` to see the list, `cancel` to exit the generator, or `send` to finish and send the Rules Section.'))
            response = await self.bot.wait_for('message',check=check_author)
            if response.content == 'new':
                await add_section()
            elif response.content == 'edit':
                await edit_section()
            elif response.content == 'view':
                embed = discord.Embed.from_dict(embedDict)
                await ctx.send(embed=embed)
                await main_menu() 
            elif response.content == 'send':
                await save_rules()
            elif response.content == 'cancel':
                pass
            else:
                await ctx.send(embed=discord.Embed(title='BrightBot Rules Generator - Error',description='Unknown Response'))
                await main_menu()

        await add_section()


    @commands.command(name='msgRole',brief='Adds reaction roles to a message.',description='`>msgRole <reactionEmoji> <roleToGive> [textInMessage]`: Standard Reaction Role command. The bot will send a message in the channel the command was run in. If you specify [textInMessage], the bot will send that message. Otherwise, it will send a preset message. ReactionEmoji should be an actual emoji. \n NOTE: The bot can only use emojis from servers it has joined.',aliases=['messageRole','MessageRole','MsgRole','MSGRole','msgrole','reactionRole','ReactionRole','reactionrole'])
    async def msgRole(self, ctx, emoji: discord.Emoji, role: discord.Role, *message):
        isAdmin = await role_checker(ctx, 'admin_commands')
        hasRole = await role_checker(ctx, role.name)
        if isAdmin:
            if hasRole:
                await ctx.message.delete()
                if str(message) != "()": 
                    botMsg = await ctx.send(" ".join(message[:]))
                else:
                    botMsg = await ctx.send(f"React with {emoji} to get the {role.name} role.")
                await botMsg.add_reaction(emoji)
                try:
                    channel = db[str(ctx.channel.id)]
                except KeyError:
                    db[str(ctx.channel.id)] = {}
                    channel = db[str(ctx.channel.id)]
                channel[str(botMsg.id)] = {"ROLE": str(role.id),"EMOJI": str(emoji.id)}

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = db.get(str(payload.channel_id), ' ')
        if channel != ' ':
            message = channel.get(str(payload.message_id), ' ')
            if message != ' ':
                if str(payload.emoji.id) == message['EMOJI']:
                    if not payload.member.bot:
                        guild = self.bot.get_guild(payload.guild_id)
                        role = guild.get_role(int(message['ROLE']))
                        await payload.member.add_roles(role)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        channel = db.get(str(payload.channel_id), ' ')
        if channel != ' ':
            message = channel.get(str(payload.message_id), ' ')
            if message != ' ':
                if str(payload.emoji.id) == message['EMOJI']:
                    guild = self.bot.get_guild(payload.guild_id)
                    target = guild.get_member(payload.user_id)
                    if not target.bot:
                        role = guild.get_role(int(message['ROLE']))
                        await target.remove_roles(role)


def setup(bot):
    bot.add_cog(message(bot))
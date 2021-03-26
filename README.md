# What is BrightBot?
BrightBot is a Discord bot written with the Discord.py library made to run on [Replit]('https://replit.com').

# What commands does BrightBot have?
Currently, I have the following commands implemented:
- **Ban** - Bans someone from the server.
- **Kick** - Kicks someone from the server.
- **Purge** - Clears messages from the chat.
- **AddRole** - Adds a certain role to someone on the server.
- **RemoveRole** - Removes a role from someone on the server.
- **Mute** - Adds the 'Mute' role to someone on the server. You will need to manually turn off the permission to send messages in channels where you don't want the muted people to talk.
- **Unmute** - Removes the 'Mute' role from someone on the server.
- **GMC** - Gets a random tweet from [Giant Military Cats](https://twitter.com/giantcat9). If you don't know what GMC is, it's a twitter account that posts ridiculous military scenes with giant cats in the middle of it all.
 - **Meme** - Gets a random meme from teh interwebz

I plan to implement more commands in the future, of course. These might include:
- **ReactionRole** - Reactions to a certain message will give users a certain role.
- **Giveaway** - Starts a giveaway

 Some commands will require the `admin_commands` role. These are commands like ban, kick, purge, addrole, removerole, mute, and unmute. This ensures only admins can run administrative commands. **Make sure only people who need those commands have that role.** You currently will need to set that role up yourself, but it's not hard - just make a role with the name `admin_commands`, you don't even need to colour it or give it permissions.

 # How do I run BrightBot?
 There are currently 2 options.
 1. **Add the bot to your server** - Just add the bot to your own server. The link is [here]('https://discord.com/api/oauth2/authorize?client_id=745433967486042133&permissions=8&scope=bot').
 2. **Run your own instance of the bot** - Because this bot is open-source, you can run it yourself! I'd recommend doing it on [Replit]('https://replit.com'), unless you have your own cloud service, because Replit is free. The only trouble is, if you are on Replit, you will need to set up some sort of bot to visit the server in `server.py` every so often (Under an hour), since if the webpage doesn't get a visit in 1 hour, Replit will stop the program. The easiest way to do this is via a website uptime monitor, like [MonitorUptime](https://monitoruptime.io) or [UptimeRobot](https://uptimerobot.com), because they are free and will connect to the website every few minutes (To see if it's up, but this will also keep your bot running.)

 # Can't I just use [insert bot name here]?
 Yeah, you're free to use whatever bot you want - however, if  you run BrightBot, you can see what is going on behind the scenes. With other bots, you don't know what's happening, and, what's more, some of them want money for basic features. That's why I have BrightBot - it's a free alternative, plus, you can run and modify it yourself.

 # Licensing
 You can view the full project license in the `LICENSE` file on this repo. However, I figured I'd summarize it here, since I made my own license (Most other licenses were long and complicated or didn't have the requirements I wanted.) It basically says anyone is free to redistribute, modify, or download this project's source code as long as you don't sell it for profit, do keep it open-source, and don't include malware, add trackers, put in ads, or restrict it's use in some way (I don't count language barriers, since translations are pretty difficult). This makes sure any other versions of my software are free, open-source, private, clean/secure, and available to everyone.
import os
from keep_alive import keep_alive
from discord.ext import commands
import discord

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(
    command_prefix="!",  # Change to desired prefix
    case_insensitive=True,
    intents=intents# Commands aren't case-sensitive
)

bot.author_id = 861939702756409344  # Change to your discord id!!!


@bot.event
async def on_ready():  # When the bot is ready
    print("I'm in")
    print(bot.user)  # Prints the bot's username and identifier


extensions = [
    'cogs.welcome'  # Same name as it would be if you were importing it
]

if __name__ == '__main__':  # Ensures this is the file being ran
    for extension in extensions:
        bot.load_extension(extension)  # Loades every extension.

keep_alive()  # Starts a webserver to be pinged.
token = os.environ.get("Auth_Token")
bot.run(token)  # Starts the bot

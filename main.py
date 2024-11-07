import os, nextcord
from dotenv import load_dotenv
from nextcord.ext import commands
load_dotenv()

bot = commands.Bot(command_prefix="=", intents=nextcord.Intents.all(), case_insensitive=True)
bot.remove_command("help")
bot.load_extensions_from_module("cogs")

bot.run(os.getenv('DISCORD_TOKEN'), reconnect=True)
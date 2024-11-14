import os, nextcord
from nextcord.ext import commands
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix="=", intents=nextcord.Intents.all(), case_insensitive=True)
bot.remove_command("help")
bot.load_extensions_from_module("cogs")

bot.run(os.getenv('DISCORD_TOKEN'), reconnect=True) 
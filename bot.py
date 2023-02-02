import discord
from discord.ext import commands
import json

with open('setting.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)
    
intents = discord.Intents.default()
intents.typing = False
intents.presences = False

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print("Bot is online")

bot.run(json_data["TOKEN"])

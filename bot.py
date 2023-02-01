import discord
from discord.ext import commands

bot = commands.bot(commands_prefix='!')

@bot.event
async def bot_online():
    print("Bot is online")

bot.run('MTA2NzM0MDAwMDE1MDE2NzYzMg.GU1MTo.CpWBdt64SZZxuaYeyq-PhH2roItZdZ7ikEJM4Q')
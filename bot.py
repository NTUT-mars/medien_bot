#導入 Discord.py
import discord
from discord.ext import commands
import json
import os

#讀取"setting.json"中的函數
with open('setting.json', 'r', encoding='UTF-8') as json_file:
    json_data = json.load(json_file)

#定義discord bot的權限，intents是我們要求的權限
#discord.intents.{}，有三種模式：all()-權限全開、default()-權限預設值、none()-權限全關
intents = discord.Intents.all()

#command_prefix：指令前面的符號
bot = commands.Bot(command_prefix='!', intents=intents)

#事件觸發：系統開機
@bot.event
async def on_ready():
    print("Bot is online")

#可以在bot還在執行中
#新增更新好的指令
@bot.command()
async def load(ctx, ext):
    bot.load_extension(f'cmds.{ext}')

#可以在bot還在執行中
#移除不要的指令
@bot.command()
async def un_load(ctx, ext):
    bot.unload_extension(f'cmds.{ext}')

#載入cmds資料夾中所有的cog
for filename in os.listdir('./cmds'):
    if filename.endswith('.py'):
        bot.load_extension(f'cmds.{filename[:-3]}')

bot.run(json_data["TOKEN"])

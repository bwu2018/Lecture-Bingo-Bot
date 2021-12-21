import os
import discord
from dotenv import load_dotenv
from CREDENTIALS import BOT_TOKEN

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        msg = 'BOOOOOOM IT WORKS'
        await message.channel.send(msg)

client.run(BOT_TOKEN)
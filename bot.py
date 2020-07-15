
import os
import random
import discord
from dotenv import load_dotenv

import OBP_per_player

teams = OBP_per_player.team()
stats = OBP_per_player.player_stat(teams)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == 'Go!':
        
        for i in range(len(stats)):
            
            response = ("Le joueur", stats[i][0], "a pour OBP", stats[i][1])
            await message.channel.send(response)

client.run(TOKEN)
import random
import os

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import discord

import OBP_per_player


bot = commands.Bot(command_prefix="b ")


teams = OBP_per_player.team()
stats = OBP_per_player.player_stat(teams)

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@bot.event
async def on_ready():
    print(f'{client.user.name} is online.')
    
    await bot.change_presence(activity=discord.Game(name="Baseball", type=3))

    
@bot.command(name="stats", help=": Affiche l'OBP de tous les joueurs.")
async def display_stat(message):


    for stat in range(len(stats)):
        
        stat_embed = discord.Embed(title=stats[i][0], description=f"__OBP :__ **{stats[i][1]}**.", color=0xff0000)
       
        await message.send(stat_embed)

            
bot.run(TOKEN)

#!/usr/bin/env python3.8.2
# -*- coding: utf-8 -*-
#
#  task_management.py
#
#  Copyright 2020 Timéo Arnouts <dogm@dogm-s-pc>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#

import os

from dotenv import load_dotenv
from discord.ext import commands
from discord.ext.commands import Bot
import discord

import OBP_per_player




load_dotenv()


TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()


bot = commands.Bot(command_prefix="bball ")



@bot.event
async def on_ready():
    """
        Affiche un message avertissant de la mise en route du bot et change le statut du bot.
    """

    print(f"{bot.user.name} is online.")

    await bot.change_presence(activity=discord.Game(name="Baseball | bball help", type=3))




@bot.command(name="stat", help=": Affiche l'OBP de tous les joueurs.")
async def display_stat(message):
    """
        Affiche l'OBP de tous les joueurs dans un embed coloré en fonction de leurs résultats.
    """

    print(f"Stat command has been called by {message.author}.")

    teams = OBP_per_player.team()
    stats = OBP_per_player.player_stat(teams)



    for j in range(len(stats)):

        if stats[j][1] is None:
            color_ = 0x5c5c5c


        # inférieur à .200 => rouge : médiocre
        elif float(stats[j][1]) < .200:
            color_ = 0xed0000

        # entre .200 et .300 => jaune : moyen
        elif float(stats[j][1]) > .200 and float(stats[j][1]) < .300:
            color_ = 0xfdee00

        # entre .300 et .500 => vert clair : bon
        elif float(stats[j][1]) > .300 and float(stats[j][1]) < .500:
            color_ = 0x149414

        # sinon => vert foncé : excellent
        else:
            color_ = 0x00561B



        stat_embed = discord.Embed(title="", description="", color=color_)

        stat_embed.add_field(name=stats[j][0], value=f"OBP:    0{stats[j][1]}")



        await message.send(embed=stat_embed)





@bot.command(name="info", help=": Affiche l'OBP du joueur mentionné en argument")
async def search_player_info(message, *player_name):
    """
        Renvoie un embed contenant les informations du joueur mentionné.
    """

    player_name = " ".join([i.title() for i in player_name])

    await message.send(f"{player_name} info is being searched.")

    print(f"Search command with argument : \"{player_name}\" was been called by {message.author}.")


    teams = OBP_per_player.team()
    stats = OBP_per_player.player_stat(teams)


    for player_info in stats:

        if player_name in player_info:

            player_obp = player_info[1]

            player_description = f"OBP : 0{player_obp}"

            break
    else:

        player_description = f"{player_name} info was not found."



    player_info_embed = discord.Embed(title=f"{player_name} informations", description=player_description, color=0x002fa7)

    player_info_embed.add_field(name=len(f"Requested by **{message.author}**")*"\_", value=f"Requested by **{message.author}**")


    await message.send(embed=player_info_embed)





bot.run(TOKEN)

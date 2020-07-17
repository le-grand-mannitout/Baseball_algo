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




@bot.command(name="stats", help=": Affiche l'OBP de tous les joueurs.")
async def display_stat(message):
    """
        Affiche l'OBP de tous les joueurs dans un embed coloré en fonction de leurs résultats.
    """


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

        # entre .300 et .500 => vert clair : bon
        elif float(stats[j][1]) > .300 and float(stats[j][1]) < .500:
            color_ = 0x149414

        # sinon => vert foncé : excellent
        else:
            color_ = 0x00561B



        stat_embed = discord.Embed(title="", description="", color=color_)

        stat_embed.add_field(name=stats[j][0], value=f"OBP:    0{stats[j][1]}")



        await message.send(embed=stat_embed)


bot.run(TOKEN)

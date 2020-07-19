
import requests  
import bs4 

import OBP_per_player


def interpretate_players_names(stats, game_url):
    
    url_compos = requests.get(game_url)

    soup = bs4.BeautifulSoup(url_compos.text, 'html.parser')

def main():

    teams = OBP_per_player.team()
    stats = OBP_per_player.player_stat(teams)
    interpretate_players_names(stats, game_url)



import requests  
import bs4 
import pickle
import sys

#del save function and replace AB/G with OBP, in a dict

def team():

    teams = []

    url_season = requests.get('https://www.baseball-reference.com/leagues/MLB/2019.shtml') 

    soup = bs4.BeautifulSoup(url_season.text, 'html.parser')
    teams_soup = soup.findAll("th", {"class":"left"})

    for i in range(32):

        teams.append(teams_soup[i].find("a"))

        if teams[-1] == None:
            del teams[-1]

        else :
            teams[-1] = teams[-1]["href"]

    return teams


def soup_to_data(soup_name):

    clean_soup = []

    for i in range (len(soup_name)):

        clean_soup.append(soup_name[i].string)

    return clean_soup

def player_stat(teams):

    stats = {}
    
    for i in range(len(teams)):

        player_list = []
        OBP_list = []
        list_tuple = []

        url_team = requests.get('https://www.baseball-reference.com' + teams[i])
        
        soup = bs4.BeautifulSoup(url_team.text, 'html.parser')
        player_soup = soup.findAll("td", {"data-stat":"player"})[:45]
        OBP_soup = soup.findAll("td", {"data-stat":"onbase_perc"})[:45]

        OBP_list = soup_to_data(OBP_soup)
        player_list = soup_to_data(player_soup)

        print(player_list)

        if i == 25 :
            del OBP_list[44:]
            del player_list[44:]

        for k in range(len(player_list)):

            list_tuple.append((player_list[k], OBP_list[k]))

        stats[teams[i]] = list_tuple

    return stats

teams = team()
stats = player_stat(teams)

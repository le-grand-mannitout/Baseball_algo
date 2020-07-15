
import requests  
import bs4 
import pickle
import sys

def team():

    teams = []

    url_season = requests.get('https://www.baseball-reference.com/leagues/MLB/2019.shtml') 

    soup = bs4.BeautifulSoup(url_season.text, 'html.parser')
    teams_soup = soup.findAll("th", {"class":"left"})
    OBP_soup = soup.findAll("td", {"data-stat":"onbase_perc"})[:30]

    OBP_list = soup_to_data(OBP_soup)

    for i in range(32):

        teams.append(teams_soup[i].find("a"))

        if teams[-1] == None:
            del teams[-1]

        else :
            teams[-1] = teams[-1]["href"]

    return teams, OBP_list


def soup_to_data(soup_name):

    clean_soup = []

    for i in range (len(soup_name)):

        clean_soup.append(soup_name[i].string)

    return clean_soup

def save(stats):

    #sys.setrecursionlimit()

    with open('C:/Users/Madil/Documents/Programmation/Python/Visual_studio/baseball_algo/save_pickle.txt', 'wb') as f:
        pickle.dump(stats[0][:2], f)

def player_stat(teams, OBP_list):

    stats = []
    
    for i in range(len(teams)):

        at_bat_per_match = []
        AB_list = []
        G_list = []
        player_list = []

        url_team = requests.get('https://www.baseball-reference.com' + teams[i])
        
        soup = bs4.BeautifulSoup(url_team.text, 'html.parser')
        player_soup = soup.findAll("td", {"data-stat":"player"})[:45]
        AB_soup = soup.findAll("td", {"data-stat":"AB"})[:45]
        G_soup = soup.findAll("td", {"data-stat":"G"})[:45]

        AB_list = soup_to_data(AB_soup)
        G_list = soup_to_data(G_soup)
        player_list = soup_to_data(player_soup)

        if i == 25 :
            del G_list[44:]
            del player_list[44:]

        for k in range(len(player_list)):

            if int(G_list[k]) != 0 :
            
                at_bat_per_match.append(int(AB_list[k]) / int(G_list[k]))
            
            else :
                at_bat_per_match.append(0)

        stats.append([teams[i], OBP_list[i], player_list, at_bat_per_match])

    return stats

teams, OBP_list = team()
stats = player_stat(teams, OBP_list)

save(stats)
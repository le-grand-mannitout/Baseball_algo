
import requests  
import bs4 

#Set OBP AB and R per player in list "stats"

#return teams, list of (team_end_url, nb_batter_in_team) tuples

def team():

    teams = []

    url_season = requests.get('https://www.baseball-reference.com/leagues/MLB/2019.shtml') 

    soup = bs4.BeautifulSoup(url_season.text, 'html.parser')
    teams_soup = soup.findAll("th", {"class":"left"})
    nb_batter_per_team_soup = soup.findAll("td", {"data-stat":"batters_used"})

    nb_batter_per_team = soup_to_data(nb_batter_per_team_soup[:30])

    for i in range(32):

        if teams_soup[i].find("a") == None:
            pass

        else :
            teams.append([teams_soup[i].find("a"), nb_batter_per_team[i]])
            teams[i][0] = teams[i][0]["href"]

    return teams


#Return a soup into list of string

def soup_to_data(soup_name):

    clean_soup = []

    for i in range(len(soup_name)):

        try :
            clean_soup.append(soup_name[i].string)

        except AttributeError:
            pass

    return clean_soup


#Scrap OBP, AB, R and players, execute soup_to_data() function and add to stats list (player, OBP, AB, R)

def player_stat(teams):

    stats = []
    
    for i in range(len(teams)):

        player_soup = []
        player_list = []
        OBP_list = []
        nb_batter = int(teams[i][1])

        url_team = requests.get('https://www.baseball-reference.com' + teams[i][0])
        
        soup = bs4.BeautifulSoup(url_team.text, 'html.parser')
        player_soup_mess = soup.findAll("td", {"data-stat":"player"})[:nb_batter]
        OBP_soup = soup.findAll("td", {"data-stat":"onbase_perc"})[:nb_batter]
        AB_soup = soup.findAll("td", {"data-stat":"AB"})
        R_soup = soup.findAll("td", {"data-stat":"R"})

        for j in range(len(player_soup_mess)):
            player_soup.append(player_soup_mess[j].find("a"))

        AB_list = soup_to_data(AB_soup)
        R_list = soup_to_data(R_soup)
        OBP_list = soup_to_data(OBP_soup)
        player_list = soup_to_data(player_soup)

        for k in range(len(player_list)):

            stats.append((player_list[k], OBP_list[k], AB_list[k], R_list[k]))

    return stats

if __name__ == "__main__":
    teams = team()
    stats = player_stat(teams)
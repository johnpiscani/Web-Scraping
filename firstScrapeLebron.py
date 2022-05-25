from bs4 import BeautifulSoup
import requests
import pandas as pd

# scraping stats on Lebron James

url = 'https://www.basketball-reference.com/players/j/jamesle01.html'

# When you print page, returns Response[200] which means successful
# between 200 and 299 is successful, HTTP response status codes if different

page = requests.get(url)

# all html lines of code in soup
soup = BeautifulSoup(page.content, 'html.parser')
# l
# columns=['Age', 'Team', 'Position', 'Games',
# 'Min', 'FG%', '3P%', 'FT%', 'REB',
# 'AST', 'STL', 'BLK', 'TOV', 'PPG']
table = soup.find('table', attrs={"class": "stats_table", "id": "per_game"})
lebronStats = pd.DataFrame()
for row in table.tbody.find_all('tr'):
    columns = row.find_all('td')
    yearStats = []
    age = columns[0].text
    yearStats.append(age)
    team = columns[1].text
    yearStats.append(team)
    # columns [2] is league
    position = columns[3].text
    yearStats.append(position)
    games = columns[4].text
    yearStats.append(games)
    # columns[5] is games started, gs = g for Lebron
    minPerGame = columns[6].text
    yearStats.append(minPerGame)
    # fgm = columns[7], fga = c[8]
    fieldGoalPercentage = columns[9].text
    yearStats.append(fieldGoalPercentage)
    # 10&11 are 3p and 3pa
    threePercentage = columns[12].text
    yearStats.append(threePercentage)
    freeThrowPercentage = columns[19].text
    yearStats.append(freeThrowPercentage)
    rebounds = columns[22].text
    yearStats.append(rebounds)
    assists = columns[23].text
    yearStats.append(assists)
    steals = columns[24].text
    yearStats.append(steals)
    blocks = columns[25].text
    yearStats.append(blocks)
    turnovers = columns[26].text
    yearStats.append(turnovers)
    points = columns[28].text
    yearStats.append(points)
    yearlyStats = pd.DataFrame(yearStats)
    lebronStats = pd.concat([lebronStats, yearlyStats], axis=1, ignore_index=True)
lebronStats = lebronStats.transpose()
lebronStats.columns = ['Age', 'Team', 'Position', 'Games',
                       'Min', 'FG%', '3P%', 'FT%', 'REB',
                       'AST', 'STL', 'BLK', 'TOV', 'PPG']
lebronStats.index = ['03/04', '04/05', '05/06', '06/07', '07/08',
                     '08/09', '09/10', '10/11', '11/12', '12/13',
                     '13/14', '14/15', '15/16', '16/17', '17/18',
                     '18/19', '19/20', '20/21', '21/22']
print(lebronStats)

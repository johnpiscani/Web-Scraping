from bs4 import BeautifulSoup
import requests
import re


class Batter:
    def __init__(self, name, war, atBats, hits, homeRuns, average):
        self.name = name
        self.war = war
        self.atBats = atBats
        self.hits = hits
        self.homeRuns = homeRuns
        self.average = average

    def __str__(self):
        return 'Name: ' + self.name + '\nWAR: ' + self.war + '\nAt Bats: ' + self.atBats + '\nHits: ' + self.hits + '\nHome runs: ' + self.homeRuns + '\nAverage: ' + self.average


class Pitcher:
    def __init__(self, name, war, wins, losses, era):
        self.name = name
        self.war = war
        self.wins = wins
        self.losses = losses
        self.era = era

    def __str__(self):
        return 'Name: ' + self.name + '\nWAR: ' + self.war + '\nWins: ' + self.wins + '\nLosses: ' + self.losses + '\nEarned Run Average: ' + self.era


def getURL(playerName):
    begURL = 'https://www.baseball-reference.com/players/'
    names = playerName.split()
    letter = names[1][0].lower()
    lastNamesURL = begURL + letter
    page = requests.get(lastNamesURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', attrs={'class': 'section_content'})
    names = div.find_all('a')
    optionList = []
    for i in names:
        if playerName in i.text:
            optionList.append(i)
    brokenURL = optionList[0]
    brokenURL = str(brokenURL)
    endURL = brokenURL.split('"')
    urlOut = 'https://www.baseball-reference.com' + endURL[1]
    return urlOut


def getPlayerData(userURL):
    page = requests.get(userURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # div which has summary of 2022 and career stats
    div = soup.find('div', attrs={"class": 'p1'})
    # finding all p tags within this div
    pList = div.find_all('p', {'class':False, 'id':False})
    removeList = []
    # adds all career stats to list
    for x in range(len(pList)):
        if x % 2 != 0:
            removeList.append(pList[x])
    # remove career stats from list of p tags
    for x in removeList:
        pList.remove(x)
    strList = []
    # put p list into new list as strings instead of bs4 element
    for x in pList:
        strList.append(str(x))
    # list for untagged data
    data = []
    # taking out the opening and closing tags for each data point
    for x in strList:
        x = re.search('<p>(.*)</p>', x)
        x = x.group(1)
        data.append(x)
    return data


def pitcherDataIntoObject(data, playerName):
    n = playerName
    wa = data[0]
    wi = data[1]
    l = data[2]
    e = data[3]
    player = Pitcher(n, wa, wi, l, e)
    return player


def batterDataIntoObject(data, playerName):
    n = playerName
    w = data[0]
    at = data[1]
    hi = data[2]
    ho = data[3]
    av = data[4]
    player1 = Batter(n, w, at, hi, ho, av)
    return player1


def main():
    # see if comparing pitchers or batters
    print('Would you like to compare pitchers or batters from the 2022 season?')
    choice = input('Enter "p" for pitchers and "b" for batters: ')
    print('Please enter the players first and last name. Nicknames will not be accepted')
    playerName1 = input("Enter first player to compare: ")
    playerName2 = input("Enter second player to compare: ")
    if choice == 'b':
        # player 1
        url1 = getURL(playerName1)
        stats1 = getPlayerData(url1)
        comp1 = batterDataIntoObject(stats1, playerName1)
        print(comp1.__str__())
        # player 2
        url2 = getURL(playerName2)
        stats2 = getPlayerData(url2)
        comp2 = batterDataIntoObject(stats2, playerName2)
        print(comp2.__str__())
    elif choice == 'p':
        # player 1
        url1 = getURL(playerName1)
        stats1 = getPlayerData(url1)
        comp1 = pitcherDataIntoObject(stats1, playerName1)
        print(comp1.__str__())
        # player 2
        url2 = getURL(playerName2)
        stats2 = getPlayerData(url2)
        comp2 = pitcherDataIntoObject(stats2, playerName2)
        print(comp2.__str__())


main()

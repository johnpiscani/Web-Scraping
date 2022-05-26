from bs4 import BeautifulSoup
import requests
import re


class Player:
    def __init__(self, name, war, atBats, hits, homeRuns, average):
        self.name = name
        self.war = war
        self.atBats = atBats
        self.hits = hits
        self.homeRuns = homeRuns
        self.average = average

    def __str__(self):
        return 'Name: ' + self.name + '\nWAR: ' + self.war + '\nAt Bats: ' + self.atBats + '\nHits: ' + self.hits + '\nHome runs: ' + self.homeRuns + '\nAverage: ' + self.average


def getURL(playerName):
    begURL = 'https://www.baseball-reference.com/players/'
    names = playerName.split()
    letter = names[1][0].lower()
    midURL = begURL + letter + '/'
    lastAbr = names[1][0:5].lower()
    firstAbr = names[0][0:2].lower()
    URL = midURL + lastAbr + firstAbr + '01.shtml'
    return URL


def getBatterData(userURL):
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


def batterDataIntoObject(data, playerName):
    n = playerName
    w = data[0]
    at = data[1]
    hi = data[2]
    ho = data[3]
    av = data[4]
    player1 = Player(n, w, at, hi, ho, av)
    return player1


def main():
    # getting names of two players
    playerName1 = input("Enter first player to compare: ")
    playerName2 = input("Enter first player to compare: ")

    url1 = getURL(playerName1)
    stats1 = getBatterData(url1)
    comp1 = batterDataIntoObject(stats1, playerName1)
    print(comp1.__str__())

    url2 = getURL(playerName2)
    stats2 = getBatterData(url2)
    comp2 = batterDataIntoObject(stats2, playerName2)
    print(comp2.__str__())


main()

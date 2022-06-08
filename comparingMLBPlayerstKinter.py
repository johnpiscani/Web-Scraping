from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
from tkinter import *


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
    firstName = names[0]
    lastName = names[1]
    letter = names[1][0].lower()
    lastNamesURL = begURL + letter
    page = requests.get(lastNamesURL)
    soup = BeautifulSoup(page.content, 'html.parser')
    div = soup.find('div', attrs={'class': 'section_content'})
    names = div.find_all('a')
    optionList = []
    for i in names:
        if firstName in i.text and lastName in i.text:
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
    pList = div.find_all('p', {'class': False, 'id': False})
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


def comparePlayers():
    player1StatLabel = Label(root, text="")
    player1StatLabel.grid(row=6, column=1)
    player2StatLabel = Label(root, text="")
    player2StatLabel.grid(row=6, column=2)
    player1StatLabel.config(text="")
    player2StatLabel.config(text="")
    playerName1 = playerOneInput.get()
    playerName2 = playerTwoInput.get()
    choice = var.get()
    if choice == 1:
        url1 = getURL(playerName1)
        stats1 = getPlayerData(url1)
        player1Obj = batterDataIntoObject(stats1, playerName1)
        url2 = getURL(playerName2)
        stats2 = getPlayerData(url2)
        player2Obj = batterDataIntoObject(stats2, playerName2)
    elif choice == 2:
        url1 = getURL(playerName1)
        stats1 = getPlayerData(url1)
        player1Obj = pitcherDataIntoObject(stats1, playerName1)
        url2 = getURL(playerName2)
        stats2 = getPlayerData(url2)
        player2Obj = pitcherDataIntoObject(stats2, playerName2)
    player1StatLabel.config(text=player1Obj.__str__())
    player2StatLabel.config(text=player2Obj.__str__())


root = Tk()
root.title("Comparing MLB Players")
var = IntVar()
# making the widgets
# labels
intro1 = Label(root, text='Welcome to the app for comparing two MLB players!')
intro2 = Label(root, text='You can compare batters or pitchers.')

player1Label = Label(root, text='Players 1: ')
player2Label = Label(root, text='Players 2: ')
playerOneInput = Entry(root, width=30)
playerTwoInput = Entry(root, width=30)

radioLabel = Label(root, text='Select type of player:')
batterRadio = Radiobutton(root, text='Batter', variable=var, value=1)
pitcherRadio = Radiobutton(root, text='Pitcher', variable=var, value=2)

compareButton = Button(root, text='Compare Players', command=comparePlayers)

# putting widgets into root on grid
intro1.grid(row=0, column=1)
intro2.grid(row=1, column=1)

radioLabel.grid(row=2, column=0)
batterRadio.grid(row=2, column=1)
pitcherRadio.grid(row=2, column=2)

player1Label.grid(row=3, column=0)
playerOneInput.grid(row=3, column=1)
player2Label.grid(row=4, column=0)
playerTwoInput.grid(row=4, column=1)

compareButton.grid(row=5, column=1)
root.mainloop()

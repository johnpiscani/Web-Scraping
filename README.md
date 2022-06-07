# Web-Scraping
my collection of projects where I work with web scraping

firstScrapeLebron.py --> first attempt using Beautiful soup, take lebrons stats from Basketball reference and put it into a pandas DF

-------------------------------------------------------------------------------------------------
compareMLBplayers may 26 2022 --> first result of comparing mlb players, everything run through the console
Notes:
- can only compare batters, not pitchers
- only has WAR, hits, at bats, hrs, average
- some players this does work (Giancarlo Stanton, name used to be mike, so url is messed up)
- ^ some players have name so URL is messed up
- player name input should be two words (fname, lname) separated by a space
What I want to add:
- pitchers stats
- if error occurs, fix it in run time, so function still runs without errors
- add visualization for stats
- add interativeness for inputting places (not through console)

--------------------------------------------------------------------------------------------------
compareMLBplayers (updated June 3 2022) --> resolved issues for some players names not coming up

Notes:
  Next time:
- Add exception handling for when input does not work bc player doesnt play vs invalid user entry
- How do I optimize user entry to prevent exception handling for happening?

Future:
- add to UI by using PyQT gui (just numbers at first)
- add visulizations to stats (using graphs/charts/etc)

--------------------------------------------------------------------------------------------------
compareMLBplayers (updated June 7 2022) --> made loop so if error, user can reinput names or p/b, prevents code from ending because user entry is wrong or there is a problem getting website/data

Next Time:
- work on TKinter mini projects to put this project into a GUI

Future:
- add visulizations for numbers for easier comparing/reading
- run app thru icon on desktop, or put in brothers fantasy baseball website

from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(START_URL)
soup = bs(page.text, "html.parser")
star_table = soup.find("table")
templist = []
table_rows = star_table.find_all("tr")
for tr in table_rows:
    td = tr.find_all("td")
    row = [i.text.rstrip()for i in td]
    templist.append(row)

starnames = []
distance = []
mass = []
radius = []
luminosity = []

for i in range(1, len(templist)):
    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    luminosity.append(templist[i][7])

df = pd.DataFrame(list(zip(starnames, distance, mass, radius, luminosity)), columns=["starnames", "distance",
 "mass", "radius", "luminosity"])
df.to_csv("brightstars.csv")
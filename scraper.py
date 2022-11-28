import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.espn.com/nba/player/gamelog/_/id/6606/damian-lillard"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

# gets some incorrect tables; want to filter from here for events_table
# tables = soup.find_all('div',class_="mb5")
# tables = soup.find_all('div',class_="events_table")

# start with 1 table
tables = soup.find('table',class_="Table")

tables_all = soup.find_all('table',class_="Table")

headers = []
for i in tables.find_all('th'):
    title = i.text
    headers.append(title)


# print(page.text)
print(tables_all[0])
print(len(tables_all))
# print(headers)

damestats = pd.DataFrame(columns = headers)

damestats_season = pd.DataFrame(columns=headers)

# -1 to remove the monthly stat row
for j in tables.find_all('tr')[1:-1]:
    row_data = j.find_all('td')
    row = [j.text for j in row_data]
    length = len(damestats)
    # print(row)
    damestats.loc[length] = row

# print(damestats)

for table in tables_all:
    for j in table.find_all('tr')[1:]:
        row_data = j.find_all('td')
        row = [j.text for j in row_data]
        length = len(damestats_season)
        if len(row) == len(headers):
            damestats_season.loc[length] = row

print(damestats_season)
# have all single game stats for games played including preseason
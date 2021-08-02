from bs4 import BeautifulSoup
import requests

def fetch_data(url: str):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'xml')
    items = soup.find_all('item')
    keys = []
    values = []

    # Loop all subelement to get title(prayer name) and description(prayer time)
    for item in items:
        title = item.find_all('title')
        desc = item.find_all('description')

        for i in title:
            keys.append(i.text) # Append to keys list

        for i in desc:
            time = i.text.split(":", 2)
            values.append("{}:{}".format(time[0], time[1]))   # Append to values list

    return dict(zip(keys, values)) 



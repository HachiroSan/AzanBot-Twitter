from bs4 import BeautifulSoup
import requests

def fetch_data(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'xml')
    items = soup.find_all('item')

    keys = []
    values = []

    # Lopp all subelement to get title(prayer name) and description(prayer time)
    for item in items:
        title = item.find_all('title')
        desc = item.find_all('description')

        for i in title:
            keys.append(i.text) # Append to keys list

        for i in desc:
            values.append(i.text)   # Append to values list

    return dict(zip(keys, values)) 



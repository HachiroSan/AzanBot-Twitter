import requests
import logging
from bs4 import BeautifulSoup
from time import sleep

logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')


def fetch_data(url: str):
    """ Get xml data from url       """
    success = False

    while not success:
        try:
            req = requests.get(url)
            success = True
        except Exception as e:
            logging.error(str(e))
            print('[Error] Unable to reach URL! Waiting 15 secs and re-trying...')
            sleep(15)

    soup = BeautifulSoup(req.text, 'xml')
    items = soup.find_all('item')
    keys = []
    values = []

    # Loop all subelement to get title(prayer name) and description(prayer time)
    for item in items:
        title = item.find_all('title')
        desc = item.find_all('description')

        for i in title:
            keys.append(i.text)  # Append to keys list

        for i in desc:
            time = i.text.split(":", 2)
            # Append to values list
            values.append("{}:{}".format(time[0], time[1]))

    return dict(zip(keys, values))  # Convert to dictionary model


""" 
{'Imsak': '05:46', 'Subuh': '05:56', 'Syuruk': '07:07', 'Zohor': '13:16', 'Asar': '16:35', 'Maghrib': '19:22', 'Isyak': '20:34'} 
"""

import requests
import logging
import datetime
from bs4 import BeautifulSoup
from time import sleep

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)


def get_xml(url):
    success = False
    while not success:
        try:
            req = requests.get(url)
            success = True
        except Exception as e:
            logging.error(str(e))
            print("[Error] Unable to reach URL! Waiting 15 secs and re-trying...")
            sleep(15)
    return req


class fetch:
    def __init__(self, url):
        req = get_xml(url)
        self.soup = BeautifulSoup(req.text, "xml")

    def get_schedule(self):
        soup = self.soup

        keys = []
        values = []

        # Loop all subelement to get title(prayer name) and description(prayer time)
        for item in soup.find_all("item"):
            for title in item.find_all("title"):
                keys.append(title.text)
            for desc in item.find_all("description"):
                time = desc.text.split(":", 2)
                values.append("{}:{}".format(time[0], time[1]))
        return dict(zip(keys, values))  # Convert to dictionary model

    def get_date(self):
        soup = self.soup

        date = soup.find("dc:date").text.split(" ", 2)
        d = datetime.datetime.strptime(date[0], "%d-%m-%Y")
        return d.strftime("%d/%m/%Y")

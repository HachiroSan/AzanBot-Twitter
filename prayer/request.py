import requests
import logging
from datetime import datetime, date
from bs4 import BeautifulSoup
from time import sleep
import csv 
from configparser import ConfigParser

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

config = ConfigParser()
config.read("config.ini")
zone_code = config.get("timezone", "ZONE")

class fetch:
    def __init__(self, url=None):
        self.url = url

    def get_schedule(self):
        url = self.url
        logging.debug('Fetching local data')
        dicts = get_csv()
        if not dicts:
            logging.debug('Unable to fetch local data! Changing to online mode')
            try:
                if not url:
                    raise Exception("URL is empty")
                logging.debug('Fetching JAKIM E-Solat data')
                dicts = get_xml(url)
                logging.debug("New schedule updated")
            except Exception as e:
                logging.error(str(e))
                raise
        return dicts

def get_csv():
    keys = ["Imsak", "Subuh", "Syuruk", "Zohor", "Asar", "Maghrib", "Isyak"]
    values = []

    today = date.today()
    _year = today.strftime('%Y')

    try:
        with open(f'./prayer/data/{_year}.csv', mode='r') as csv_file:
            csv_reader = csv.DictReader(csv_file)

            for row in csv_reader:
                if row["Zon"] == zone_code:
                    date_col = datetime.strptime(row["Tarikh"], '%d/%m/%Y').strftime('%d/%m/%Y')
                    if date_col == today.strftime('%d/%m/%Y'):
                        for i in keys:
                            values.append(datetime.strptime(row[i], '%H:%M:%S').strftime('%H:%M'))
    except IOError as e:
        logging.debug(str(e))
    except Exception as e:
        logging.error(str(e))

    return dict(zip(keys, values))

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

    soup = BeautifulSoup(req.text, "xml")

    keys = []
    values = []

    # Loop all subelement to get title(prayer name) and description(prayer time)
    for item in soup.find_all("item"):
        for title in item.find_all("title"):
            keys.append(title.text)
        for desc in item.find_all("description"):
            time = datetime.strptime(desc.text, '%H:%M:%S').strftime('%H:%M')
            values.append(time)

    try:
        dicts = dict(zip(keys, values))
        if not dicts:
            raise Exception("Dictionary returns empty")
    except Exception as e:
        logging.error(str(e))
        raise

    return dicts  # Convert to dictionary model
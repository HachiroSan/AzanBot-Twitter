from prayer import system, twitter
from prayer.request import fetch
from time import sleep
import schedule
import logging
from datetime import datetime, timedelta

logging.basicConfig(
    filename="debug.log",
    level=logging.DEBUG,
    format="%(asctime)s:%(levelname)s:%(message)s",
)

url = "https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon={}".format(
    twitter.zone_code
)

# Log update count
_counter = 0

# Default notification, To exclude notification, remove from list
_notification = ["Imsak", "Subuh", "Syuruk", "Zohor", "Asar", "Maghrib", "Isyak"]


def initialize_once():
    """running once"""

    sys_timezone = "[INFO]\nSystem time zone\t: " + system.get_timezone()
    pry_timezone = "\nPrayer time zone\t: " + twitter.zone_code
    send_solat_enabled = "\nNotification enabled\t: " + ", ".join(_notification) + "\n"
    msg = "\n[AzanBot] Running for the first time"

    dashboard = sys_timezone + pry_timezone + send_solat_enabled + msg

    print(dashboard)

    logging.debug("Running for the first time")

    initialize_once.__code__ = (lambda: None).__code__


def update_prayer():
    """Update new job schedule"""

    global _counter
    if _counter == 0:  # if first time running
        print("[AzanBot] Updating praying time")
        logging.debug("Updating praying time")
        print("[AzanBot] Scheduler is running")
    else:
        print("{} Updating new prayer time".format(system.get_timedate("[%d-%m-%Y][%I:%M %p]")))
        logging.debug("Updating new prayer time")
    _counter += 1

    create_job()


def create_job():

    schedule.clear()
    schedule.every().day.at("00:01").do(update_prayer)

    obj = fetch(url)
    dicts = obj.get_schedule()

    for i in dicts:
        if i == 'Imsak':
            schedule.every().day.at(dicts[i]).do(create_jadual_solat, schedule=dicts, date=system.get_timedate("%d/%m/%Y"))
            continue
        schedule.every().day.at(dicts[i]).do(create_solat, prayer=i)


def create_jadual_solat(schedule, date):
    """Create jadual solat notification msg"""

    msg_send_solat = "Jadual waktu solat {} : Imsak ({}), Subuh ({}), Syuruk ({}), Zohor ({}), Asar ({}), Maghrib ({}), Isyak ({}).".format(
        date,
        system.convert_12hrs(schedule["Imsak"]),
        system.convert_12hrs(schedule["Subuh"]),
        system.convert_12hrs(schedule["Syuruk"]),
        system.convert_12hrs(schedule["Zohor"]),
        system.convert_12hrs(schedule["Asar"]),
        system.convert_12hrs(schedule["Maghrib"]),
        system.convert_12hrs(schedule["Isyak"]),
    )
    send_tweet(msg_send_solat)


def create_solat(prayer):
    """Create solat notification msg"""

    if prayer in _notification:
        if prayer not in ("Imsak", "Syuruk"):
            addin = "solat fardhu {}".format(prayer)
        else:
            addin = prayer

    custom_msg = twitter.msg
    msg = custom_msg.format(timestamp_12hr=system.get_timedate('%I:%M %p'), timestamp_24hr=system.get_timedate('%H:%M'), prayer=addin)

    send_tweet(msg)


def send_tweet(msg):
    """Send tweet"""

    logging.debug(msg)
    try:
        twitter.api.update_status(msg)
    except Exception as e:
        logging.error("Twitter update failed!")
    return None


if __name__ == "__main__":
    system.clear()
    initialize_once()
    update_prayer()
    while True:
        schedule.run_pending()
        sleep(1)

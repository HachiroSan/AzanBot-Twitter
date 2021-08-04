from prayer import request, system, twitter
from time import sleep
import schedule
import logging

logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon={}'.format(twitter.zone_code)

_counter = 0     # Log update interval
_notification = ['Subuh', 'Zohor', 'Asar', 'Maghrib', 'Isyak']  # Default notification, Imsak Syuruk excluded


def initialize():

    system.clear()

    sys_timezone = '[INFO]\nSystem time zone\t: ' + system.get_timezone()
    pry_timezone = '\nPrayer time zone\t: ' + twitter.zone_code
    notify_enabled = '\nNotification enabled\t: ' + ', '.join(_notification) +'\n'
    msg1 = '\n[AzanBot] Running for the first time'

    print(sys_timezone+pry_timezone+notify_enabled+msg1)
    logging.debug('Running for the first time')

    update_prayer()

    initialize.__code__ = (lambda: None).__code__


def notify(prayer):
    if prayer in _notification:
        msg_notify = '{} Telah masuk waktu solat fardu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan-kawasan yang sewaktu dengannya.'.format(system.get_time(), prayer)
        logging.debug(msg_notify)
        try:
            twitter.api.update_status(msg_notify + '  #PrayerReminder')
            # twitter.api.update_status('Telah masuk waktu solat fardu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan-kawasan yang sewaktu dengannya.'.format(prayer))
        except Exception as e:
            logging.error('Twitter update failed!')


def update_prayer():
    global _counter

    if _counter:

        print('{} Updating new prayer time'.format(system.get_time()))
        logging.debug('Updating new prayer time')

    else:

        print('[AzanBot] Updating praying time')
        logging.debug('Updating praying time')

    schedule.clear()
    schedule.every().day.at("00:01").do(update_prayer) 

    try:
        dicts = request.fetch_data(url)  

        if not dicts:
            raise Exception('Dictionary returns empty')

        logging.debug('New schedule updated')
        print('[AzanBot] New schedule updated')

    except Exception as e:
        logging.error(str(e))
        raise
        
    for i in dicts:
        schedule.every().day.at(dicts[i]).do(notify, prayer=i)   
    
    print('[AzanBot] Scheduler is running')

    _counter += 1


if __name__ == "__main__":
    initialize()
    while True:
        schedule.run_pending()
        sleep(1)

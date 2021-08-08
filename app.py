from prayer import request, system, twitter
from time import sleep
import schedule
import logging
from datetime import datetime, timedelta

logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon={}'.format(
    twitter.zone_code)

# Log update count
_counter = 0

# Default notification, To exclude notification, remove from list
_notification = ['Imsak', 'Subuh', 'Syuruk',
                 'Zohor', 'Asar', 'Maghrib', 'Isyak']


def initialize():
    """ Initialize for the first run only   """
    system.clear()

    sys_timezone = '[INFO]\nSystem time zone\t: ' + system.get_timezone()
    pry_timezone = '\nPrayer time zone\t: ' + twitter.zone_code
    notify_enabled = '\nNotification enabled\t: ' + \
        ', '.join(_notification) + '\n'
    msg1 = '\n[AzanBot] Running for the first time'

    print(sys_timezone+pry_timezone+notify_enabled+msg1)
    logging.debug('Running for the first time')

    update_prayer()

    initialize.__code__ = (lambda: None).__code__


def notify(prayer, schedule={}):
    """ Send notification to terminal and twitter   """

    if prayer == 'schedule':
        msg_notify = ('Jadual waktu solat {} : Imsak ({}), Subuh ({}), Syuruk ({}), Zohor ({}), Asar ({}), Maghrib ({}), Isyak ({}).'
                      .format(system.get_current_date(),
                              system.convert_12hrs(schedule['Imsak']),
                              system.convert_12hrs(schedule['Subuh']),
                              system.convert_12hrs(schedule['Syuruk']),
                              system.convert_12hrs(schedule['Zohor']),
                              system.convert_12hrs(schedule['Asar']),
                              system.convert_12hrs(schedule['Maghrib']),
                              system.convert_12hrs(schedule['Isyak'])))

        logging.debug(msg_notify)

        try:
            # # posting the tweet
            twitter.api.update_status(msg_notify)
        except Exception as e:
            logging.error('Twitter update failed!')

        return None

    if prayer in _notification:

        if prayer in ('Imsak', 'Syuruk'):   # Custom msg for Imsak and Syuruk
            msg_notify = '{} Telah masuk waktu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan yang sewaktu dengannya.'.format(
                system.get_time(), prayer)
        else:
            msg_notify = '{} Telah masuk waktu solat fardhu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan yang sewaktu dengannya.'.format(
                system.get_time(), prayer)

        logging.debug(msg_notify)

        try:
            # # posting the tweet
            twitter.api.update_status(msg_notify + '  #PrayerReminder')
        except Exception as e:
            logging.error('Twitter update failed!')


def update_prayer():
    """ Update new prayer's job schedule """

    global _counter

    if _counter == 0:  # if first time running
        print('[AzanBot] Updating praying time')
        logging.debug('Updating praying time')
    else:
        print('{} Updating new prayer time'.format(system.get_time()))
        logging.debug('Updating new prayer time')

    schedule.clear()
    # Update prayer at 0001 or 12:01 AM everyday
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

    # Minus 5 minutes from Fajr Prayer
    daily_schedule = datetime.strptime(
        dicts['Subuh'], '%H:%M') - timedelta(hours=0, minutes=5)
    schedule.every().day.at(daily_schedule.strftime('%H:%M')).do(notify, prayer='schedule',
                                                                 schedule=dicts)  # Send prayer schedule of the day 5 minutes before Fajr/Subuh

    for i in dicts:
        schedule.every().day.at(dicts[i]).do(notify, prayer=i)

    print('[AzanBot] Scheduler is running')

    _counter += 1


if __name__ == "__main__":
    initialize()
    while True:
        schedule.run_pending()
        sleep(1)

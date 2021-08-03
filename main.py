import request
import time
import schedule
import logging
import twitter

logging.basicConfig(filename='debug.log', level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s:%(message)s')

_update = 0

url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon={}'.format(twitter.zone_code)

def initialize():
    print('[AzanBot] Running for the first time')
    logging.debug('Running for the first time')
    update_prayer()
    initialize.__code__ = (lambda: None).__code__

def notify(prayer):
    t = time.strftime("[%I:%M %p]")
    print('{} Sudah masuk waktu solat fardu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan-kawasan yang sewaktu dengannya.'.format(t, prayer))

def update_prayer():
    global _update
    t = time.strftime("[%I:%M %p]")
    if _update:
        print('{} Updating new prayer time'.format(t))
        logging.debug('Updating new prayer time')
    else:
        print('[AzanBot] Updating praying time')
        logging.debug('Updating praying time')
    schedule.clear()
    schedule.every().day.at("21:44").do(update_prayer) 
    _update += 1

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

if __name__ == "__main__":
    initialize()
    print('[AzanBot] Scheduler is running')
    while True:
        schedule.run_pending()
        time.sleep(1)

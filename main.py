import request
import time
import schedule

url = 'https://www.e-solat.gov.my/index.php?r=esolatApi/xmlfeed&zon=PHG02'

def initialize():
    print('[LOG] Running for the first time')
    update_prayer()
    initialize.__code__ = (lambda: None).__code__

def notify(prayer):
    t = time.strftime("[%I:%M %p]")
    print('{} Sudah masuk waktu solat fardu {} bagi kawasan Kuantan, Pekan, Rompin dan Muadzam Shah serta kawasan-kawasan yang sewaktu dengannya.'.format(t, prayer))

def update_prayer():
    print('[LOG] Updating praying time')
    schedule.clear()
    schedule.every().day.at("00:00").do(update_prayer) 
    dicts = request.fetch_data(url)  
    for i in dicts:
        schedule.every().day.at(dicts[i]).do(notify, prayer=i)   

if __name__ == "__main__":
    initialize()
    print('[LOG] Scheduler is running...')
    while True:
        schedule.run_pending()
        time.sleep(1)

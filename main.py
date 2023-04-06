from twitter import Tweety
from scheduler import Scheduler
from azan import AzanFetcher
from utils import printl, tz
from datetime import datetime, timedelta


class AzanBot:
    def __init__(self):
        # Initiate class
        self.Tweety = Tweety()
        self.Scheduler = Scheduler()
        self.Azan = AzanFetcher()

        # Start the bot
        self.main()

    def main(self):
        self.add_twitter_notification_jobs()
        # printl(self.Azan.get_next_azan_time())

    def add_twitter_notification_jobs(self, **kwargs):
        global tz

        # Check if the function is called by the scheduler
        called_by_scheduler = kwargs.get("called_by_scheduler", False)
        if called_by_scheduler:
            printl("Refreshing Azan schedule...")

        Scheduler = self.Scheduler
        # clear all jobs
        Scheduler.clear_schedule()
        # refresh new Azan schedule
        self.Azan.refresh()
        AzanSchedule = self.Azan.AzanSchedule

        HASHTAG = "#WaktuSolat #RamadanKareem"
        message = {
            "imsak": f"Telah masuk waktu Imsak ({AzanSchedule['imsak']}) bagi kawasan Kuantan dan kawasan sewaktu dengannya. Waktu solat pada hari ini. Imsak ({AzanSchedule['imsak']}), Subuh ({AzanSchedule['fajr']}), Syuruk ({AzanSchedule['syuruk']}), Zohor ({AzanSchedule['dhuhr']}), Asar ({AzanSchedule['asr']}), Maghrib ({AzanSchedule['maghrib']}), Isyak({AzanSchedule['isha']}). \n{HASHTAG}",
            "fajr": f"Telah masuk waktu solat fardhu Subuh ({AzanSchedule['fajr']}) bagi kawasan Kuantan dan kawasan yang sewaktu dengannya. Waktu seterusnya adalah Syuruk ({AzanSchedule['syuruk']}). {HASHTAG}",
            "syuruk": f"Telah masuk waktu Syuruk ({AzanSchedule['syuruk']}) bagi kawasan Kuantan dan kawasan sewaktu dengannya. Waktu seterusnya adalah Zohor ({AzanSchedule['dhuhr']}). {HASHTAG}",
            "dhuhr": f"Telah masuk waktu solat fardhu Zohor ({AzanSchedule['dhuhr']}) bagi kawasan Kuantan dan kawasan sewaktu dengannya. Waktu seterusnya adalah Asar ({AzanSchedule['asr']}). {HASHTAG}",
            "asr": f"Telah masuk waktu solat fardhu Asar ({AzanSchedule['asr']}) bagi kawasan Kuantan dan kawasan sewaktu dengannya. Waktu seterusnya adalah Syuruk ({AzanSchedule['maghrib']}). {HASHTAG}",
            "maghrib": f"Telah masuk waktu solat fardhu Maghrib ({AzanSchedule['maghrib']}) bagi kawasan Kuantan dan kawasan sewaktu dengannya. Waktu seterusnya adalah Isyak ({AzanSchedule['isha']}). {HASHTAG}",
            "isha": f"Telah masuk waktu solat fardhu Isyak ({AzanSchedule['isha']}) bagi kawasan Kuantan dan kawasan yang sewaktu dengannya. {HASHTAG}",
        }

        current_time = datetime.now(tz).time()

        for prayer_name, prayer_time in AzanSchedule.items():
            if prayer_name == "date" or prayer_name == "hijri" or prayer_name == "day":
                continue
            # Parse prayer_time string to datetime.time object
            time = datetime.strptime(prayer_time, "%H:%M").time()

            # Check if prayer_time has already passed
            if time <= current_time:
                printl(f"{prayer_name} ({prayer_time}) has already passed today.")
                # If it's Isha, we're finished for today
                if prayer_name == "isha":
                    printl(
                        "No more prayer today, scheduling tomorrow's prayer at 12:05 AM"
                    )
                continue

            Scheduler.add_schedule(
                self.notify,
                "date",
                run_date=datetime.now(tz).replace(
                    hour=time.hour,
                    minute=time.minute,
                ),
                args=[message[prayer_name], prayer_name],
                timezone=tz,
            )
            printl(
                f"{prayer_name} time at {time.strftime('%H:%M')} has been scheduled."
            )

        # Schedule refresh_daily() to run at 12:05 AM
        self.add_daily_refresh()

    def add_daily_refresh(self):
        global tz
        Scheduler = self.Scheduler
        next_day = datetime.now(tz) + timedelta(days=1)
        run_time = datetime.combine(next_day, datetime.min.time()) + timedelta(
            minutes=5
        )
        Scheduler.add_schedule(
            self.add_twitter_notification_jobs,
            "date",
            run_date=run_time,
            args=[],
            kwargs={"called_by_scheduler": True},
            timezone=tz,
        )

    def notify(self, message, prayer_name):
        if self.Tweety.post_tweet(message):
            printl(f"{prayer_name} tweeted successfully.")
        else:
            printl(f"{prayer_name} failed to tweet.")

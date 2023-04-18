import requests
from config import TIMEZONE, ZONE
from datetime import datetime, timedelta
from utils import printl, tz


class AzanFetcher:
    def __init__(self):
        self.timezone = TIMEZONE
        self.zone = ZONE
        self.url = "https://www.e-solat.gov.my/index.php?r=esolatApi/TakwimSolat&period=today&zone={}".format(
            self.zone
        )
        self.response = self.get_response()
        self.AzanSchedule = self.get_prayer_times_by_zone()

    def get_response(self):
        # Make a GET request to the API
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # raise exception if HTTP response is not 200 OK
        except requests.exceptions.HTTPError as http_err:
            printl(f"HTTP error occurred: {http_err}", hidden=True)
            return None
        except requests.exceptions.RequestException as err:
            printl(f"Other error occurred: {err}", hidden=True)
            return None
        return response

    def get_prayer_times_by_zone(self):
        """_summary_

        Returns:
            _type_: _description_
        """

        # Parse the JSON response
        azan_time = {}
        data = self.response.json()

        # Loop through the prayer time data and store it in the dictionary
        for prayer in data["prayerTime"]:

            # Convert the data from integer date to string date in hijri
            hijri_year, hijri_month, hijri_day = prayer["hijri"].split("-")
            hijri_month_name = {
                "01": "Muharram",
                "02": "Safar",
                "03": "Rabiul Awal",
                "04": "Rabiul Akhir",
                "05": "Jumadil Awal",
                "06": "Jumadil Akhir",
                "07": "Rajab",
                "08": "Syaban",
                "09": "Ramadan",
                "10": "Syawal",
                "11": "Zulhijjah",
                "12": "Muharram"
            }[hijri_month]
            prayer["hijri"] = f"{hijri_day} {hijri_month_name} {hijri_year}"

            # Create a dictionary to convert the day from English to Malay
            english_to_malay = {
                "Monday": "Isnin",
                "Tuesday": "Selasa",
                "Wednesday": "Rabu",
                "Thursday": "Khamis",
                "Friday": "Jumaat",
                "Saturday": "Sabtu",
                "Sunday": "Ahad",
            }
            # Convert the day from English to Malay
            prayer["day"] = english_to_malay[prayer["day"]]

            azan_time = {
                "jadual": (datetime.strptime(prayer['imsak'][:-3], '%H:%M') - timedelta(minutes=10)).strftime('%H:%M'), # We will post the jadual during 10 minutes before imsak time
                "date": datetime.strptime(prayer["date"], '%d-%b-%Y').strftime('%d %B %Y'), # Convert from string to datetime object and then to string again
                "hijri": prayer["hijri"],
                "day": prayer["day"],
                "imsak": prayer["imsak"][:-3],  # remove trailing second
                "fajr": prayer["fajr"][:-3],
                "syuruk": prayer["syuruk"][:-3],
                "dhuhr": prayer["dhuhr"][:-3],
                "asr": prayer["asr"][:-3],
                "maghrib": prayer["maghrib"][:-3],
                "isha": prayer["isha"][:-3],
            }

        return azan_time

    def get_next_azan_time(self):
        """Returns the next scheduled azan time based on the current time in the timezone provided.

        Returns a dictionary with a single key-value pair representing the next scheduled azan time and its corresponding time value.

        Args:
            self: An instance of the AzanScheduler class.

        Returns:
            A dictionary with a single key-value pair representing the next scheduled azan time and its corresponding time value. The key is a string indicating the type of azan, and the value is a string representing the scheduled time in the format 'HH:MM:SS'.
        """
        global tz
        AzanSchedule = self.AzanSchedule
        current_time = datetime.now(tz).time()

        if current_time < datetime.strptime(AzanSchedule["fajr"], "%H:%M").time():
            return {"fajr": AzanSchedule["fajr"]}
        elif current_time < datetime.strptime(AzanSchedule["syuruk"], "%H:%M").time():
            return {"syuruk": AzanSchedule["syuruk"]}
        elif current_time < datetime.strptime(AzanSchedule["dhuhr"], "%H:%M").time():
            return {"dhuhr": AzanSchedule["dhuhr"]}
        elif current_time < datetime.strptime(AzanSchedule["asr"], "%H:%M").time():
            return {"asr": AzanSchedule["asr"]}
        elif current_time < datetime.strptime(AzanSchedule["maghrib"], "%H:%M").time():
            return {"maghrib": AzanSchedule["maghrib"]}
        elif current_time < datetime.strptime(AzanSchedule["isha"], "%H:%M").time():
            return {"isha": AzanSchedule["isha"]}
        else:
            return None

    def refresh(self):
        self.response = self.get_response()
        self.AzanSchedule = self.get_prayer_times_by_zone()

import pandas as pd
import requests
from datetime import datetime
import pytz

CSV_FILE = "timezone.csv"


def checkTimeZone(timezone):
    """Parse the timezone data from csv file"""
    df = pd.read_csv(CSV_FILE)

    # Check if column 'A' contains the string 'AN' (case-insensitive)
    if df["zone"].str.contains(timezone, case=False).any():
        index = df.loc[df["zone"].str.contains(timezone, case=False)].index[0]
        return df.at[index, "zone"]

    elif df["locale"].str.contains(timezone, case=False).any():
        index = df.loc[df["locale"].str.contains(timezone, case=False)].index[0]
        return df.at[index, "zone"]

    else:
        return False


def get_locale_from_Timezone(timezone):
    """Parse the timezone data from csv file"""
    df = pd.read_csv(CSV_FILE)

    # Check if column 'A' contains the string 'AN' (case-insensitive)
    if df["zone"].str.contains(timezone, case=False).any():
        index = df.loc[df["zone"].str.contains(timezone, case=False)].index[0]
        return df.at[index, "zone"], df.at[index, "locale"]

    elif df["locale"].str.contains(timezone, case=False).any():
        index = df.loc[df["locale"].str.contains(timezone, case=False)].index[0]
        return df.at[index, "zone"], df.at[index, "locale"]

    else:
        return False


def post_tweet(tweety, azan_type, time, location, logcontainer):
    """Post Azan notification to Twitter

    Args:
        tweety (tweety): Tweety instance
        azan_type (_type_): Azan type e.g Subuh, Dzuhur, Asar, Maghrib, Isyak
        time (_type_): Azan time
    """
    tweet_msg = getMessages(azan_type, time, location)
    try:
        tweety.api.update_status(tweet_msg)
        logcontainer.add_log(f"Azan Notified Successfully: '{azan_type}'")
    except tweety.TweepError as e:
        logcontainer.add_log(
            f"Unable to post tweet. Please check your credentials: {e}"
        )


def getMessages(azan_type, time, location) -> str:
    """Return full string of azan notificaiton messages including Azantype and full timezone

    Args:
        azanType (string): Type of azan e.g Subuh, Dzuhur, Asar, Maghrib, Isyak
        time (DateTime Object): Only hours and minutes are used
        location (string): Location of the azan

    Returns:
        string: notification messages
    """
    zone, locale = get_locale_from_Timezone(location)
    if azan_type == "imsak" or azan_type == "syuruk":
        return f"Telah masuk waktu {azan_type.capitalize()} pada [{time.strftime('%H:%M')}] bagi kawasan {locale} dan kawasan yang sewaktu dengannya. #WaktuSolat"
    else:
        return f"Telah masuk waktu solat fardhu {azan_type.capitalize()} pada [{time.strftime('%H:%M')}] bagi kawasan {locale} dan kawasan yang sewaktu dengannya. #WaktuSolat"


def get_Azan_Schedule_from_API(zone_name):
    # Make a GET request to the API
    response = requests.get(
        f"https://waktu-solat-api.herokuapp.com/api/v1/prayer_times.json?zon={zone_name}"
    )
    # Parse the JSON response
    azantime = {}
    data = response.json()
    for key in data["data"][0]["waktu_solat"]:
        azantime.update({key["name"]: key["time"]})

    return azantime


def get_next_azan_time(azan_schedule):
    """Return the next azan time from the azan schedule

    Args:
        azan_schedule (dict): Dictionary of azan schedule

    Returns:
        string: Next azan time
    """
    # Use Malaysia timezone
    tz = pytz.timezone("Asia/Kuala_Lumpur")
    # parse the times into datetime objects with the current year, month, and day
    azan_schedule = {
        k: tz.localize(
            datetime.strptime(v, "%H:%M").replace(
                year=datetime.now().year,
                month=datetime.now().month,
                day=datetime.now().day,
            )
        )
        for k, v in azan_schedule.items()
    }

    # get the current time
    now = datetime.now(tz)

    # sort the dictionary by the values (i.e. times)
    sorted_azan_schedule = sorted(azan_schedule.items(), key=lambda x: x[1])

    # find the first value (i.e. time) that is after the current time
    closest_time = None
    for key, value in sorted_azan_schedule:
        if value > now:
            closest_time = value
            break

    if not closest_time:
        # if there is no time after the current time, then the closest time is the first time
        closest_time = sorted_azan_schedule[0][1]

    # get the key of the closest time
    closest_key = next(
        key for key, value in sorted_azan_schedule if value == closest_time
    )

    # print(closest_time.strftime("%H:%M"))
    # get duration between now and the closest time
    # duration = closest_time - now

    return closest_key

from time import strftime, gmtime
import datetime
from subprocess import getoutput
from os import system, name


def clear():
    """Clear screen for both windows and linux"""
    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


def get_timezone():
    """Get time zone"""
    # for windows
    if name == "nt":
        return (
            strftime("%z ", gmtime())
            + datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
        )

    # for mac and linux(here, os.name is 'posix')
    else:
        location = getoutput("cat /etc/timezone")
        timezone = getoutput("date +%z")

        return timezone + " " + location


def get_timedate(format):
    """get current time"""
    return strftime(format)
    
def convert_12hrs(hrs_24):
    """Convert 24 hours to 12 hours"""
    d = datetime.datetime.strptime(hrs_24, "%H:%M")
    return d.strftime("%I:%M %p")

import datetime
import pytz
from config import TIMEZONE

tz = pytz.timezone(TIMEZONE)  # set timezone


def printl(*args, hidden=False, log_file="log.txt", **kwargs):
    # Get the current time in the specified timezone, or use local time if no timezone is specified
    now = datetime.datetime.now(tz)

    # Format the date and time as desired
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    # Add the timestamp to the message and call the built-in print function
    message = f"[{timestamp}] " + " ".join(str(arg) for arg in args)
    if not hidden:
        print(message, **kwargs)

    # Write the message to the log file if not hidden or if explicitly requested
    if not hidden or kwargs.get("log", False):
        with open(log_file, "a+") as f:
            f.write(message + "\n")

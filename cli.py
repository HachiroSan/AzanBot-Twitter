import argparse
from main import AzanBot
from func import checkTimeZone, get_locale_from_Timezone
import sys
import colorama

parser = argparse.ArgumentParser(prog="twint", usage="python3 %(prog)s [options]")
parser.add_argument("-t", "--timezone", help="city, state or timezone to be used")
args = parser.parse_args()

# Check if timezone exists in the csv file args.timezone
row_index = checkTimeZone(args.timezone)
if not row_index:
    print("Invalid timezone")
    sys.exit(1)
else:
    zone, locale = get_locale_from_Timezone(args.timezone)
    choice = input(
        "Please verify if this is the correct timezone: \n"
        + f"[{zone}] : "
        + locale
        + " (y/n): "
    )
    if choice == "n":
        sys.exit(1)
    else:
        AzanBot(args.timezone).run()

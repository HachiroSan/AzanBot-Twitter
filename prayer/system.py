from time import strftime, gmtime
import datetime
from subprocess import getoutput
from os import system, name

today = datetime.date.today()

def clear():
  
    # for windows
    if name == 'nt':
        _ = system('cls')
  
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def get_timezone():
    
    # for windows
    if name == 'nt':
        return strftime("%z ", gmtime()) + datetime.datetime.now(datetime.timezone.utc).astimezone().tzname()
  
    # for mac and linux(here, os.name is 'posix')
    else:
        location = getoutput("cat /etc/timezone")
        timezone = getoutput("date +%z")
        
        return timezone + ' ' + location
        
    
def get_time():
    return strftime("[%I:%M %p]")

def get_current_date():
    return today.strftime("%d/%m/%y")
    
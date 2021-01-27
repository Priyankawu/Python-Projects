from datetime import datetime, timedelta #module datetime- contains several classes, date is an object
#datetime module, datetime class, date object

import time
#from pytz import timezone #? Why import separately when below I imported all
import pytz #utc, timezone(), now(), astimezone()

#find current time in Portland, NYC and London

tz_Portland = pytz.timezone("US/Pacific") #how do I read this?
tz_NYC = pytz.timezone("US/Eastern")
tz_London = pytz.timezone("Europe/London")


fmt = '%H'
nowP = datetime.now(tz_Portland)
nowN = datetime.now(tz_NYC)
nowL = datetime.now(tz_London)


print(nowP.hour)
print(nowN)
print(nowL)

#Check to see if its from 9-5. Print.
def check_hours(dt_object):
    if (dt_object.hour >=9 and dt_object.hour <17):
        print("open hours")
    else:
        print("closed hours")
check_hours(nowP)
check_hours(nowN)
check_hours(nowL)











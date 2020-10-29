# /usr/bin/python

'''
"naive" and "aware" objects
You need to read the top of the datetime docs, which explain about timezones and "naive" and "aware" objects.
If your original naive datetime was UTC, the way to recover it is to use utcfromtimestamp instead of fromtimestamp.

'''

import time
import datetime

today_date = datetime.datetime.today()
print("Today date")
print(today_date)

print(today_date.year)
print(today_date.month)
print(today_date.day)

# +ve number in timedelta() will increased the date, -ve number will decrease
dt = datetime.timedelta(50)
new_date = today_date + dt
print(new_date)
print(type(new_date))


def stringtotimeobj(string, format_string="%m/%d/%Y %H:%M"):
    tuple = time.strptime(string, format_string)
    return int(time.mktime(tuple))


print(stringtotimeobj("01/01/2000 12:00"))
print(stringtotimeobj("01/01/2000", "%m/%d/%Y"))

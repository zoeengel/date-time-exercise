from datetime import date
from datetime import time, timedelta
from datetime import datetime

d=date(2013, 8, 22)
print(d. year)
print(d. month)
print(d. day)
print(d. strftime("%y-%m-%d"))

t=time(3, 54, 34)
print(t. hour)
print(t. minute)
print(t. second)
print(t. strftime("%H:%M:%S"))

dt=datetime(2015, 10, 16, 11, 22, 45)
#get datetime after 5 days
add_dt=dt + timedelta(days=5)
print(add_dt. strftime("%d-%m-%y %H:%M:%S")) 


dates = datetime(2020, 10, 16)
x = 0
while x<10:
    print(dates)
    dates=dates + timedelta(days=14)
    x = x + 1

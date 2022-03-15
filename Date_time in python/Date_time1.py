import datetime # Python provides built_in meodule datetime,from that we access class,method....
dt=datetime.datetime.now()
print("Current Date and Time:",dt)

# created current datetime object containing current local date and time

#Print today's year, month and day

from datetime import date

# date object of today's date
today = date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)
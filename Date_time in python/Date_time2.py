# Get current date
import datetime

from datetime import date

dt=datetime.date.today() # here we are using date class from the datetime module,and today() method to extract today date
print("today's date is:",dt)
# Get date from a timestamp
timestamp = date.fromtimestamp(326244364)
print("Date :", timestamp)
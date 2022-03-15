import datetime
print(dir(datetime)) ## 'dir' is used to get all the available attributes that are present in the datetime module
#Date object to represent a date
d = datetime.date(2019, 10, 30)
print(d)


from datetime import date
d=date(2021,10,30)
print(d)
#Get current date
today = date.today()

print("Current date :", today)

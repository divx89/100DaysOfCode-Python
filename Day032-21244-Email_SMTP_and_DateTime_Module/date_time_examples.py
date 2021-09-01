import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
print(now)
print(year)
print(month)
print(now.day)
print(now.weekday())

date_of_birth = dt.datetime(year=1980, month=1, day=1, hour=18, minute=30, second=20)
print(date_of_birth)

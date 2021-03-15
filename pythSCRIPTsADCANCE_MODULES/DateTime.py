'''
DATETIME
'''
import datetime
myTime = datetime.time(2, 20,1,100)
print(myTime.minute)
print(myTime.hour)
print(myTime)
print(myTime.microsecond)

'''
DATE
'''
today = datetime.date.today()
print(today)
print("YEAR : " + str(today.year))
print("MONTH: " + str(today.month))
print("DAY " + str(today.day))
print(today.ctime())
from datetime import datetime
mydtime = datetime(2021, 10, 20, 13, 10, 50, 100)
print(mydtime)
mydtime = mydtime.replace(year=2020)
print(mydtime)
from datetime import date
date1 = date(1998, 11, 3)
date2 = date(1999, 11, 3)
# returning the differents in days
print(date2 - date1)
datetime1 = datetime(1998, 11, 3, 22, 0)
datetime2 = datetime(1999, 11, 3, 12, 0)
print(datetime2 - datetime1)
dif = datetime1 - datetime2
print(dif.total_seconds())

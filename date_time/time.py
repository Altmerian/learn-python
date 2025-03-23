import time
import datetime
import calendar

time1 = time.time()
time2 = time.localtime(time1)

# Define a tuple representing a time (year, month, day, hour, minute, second, weekday, yearday, isdst)
time_tuple = (2025, 3, 21, 15, 30, 0, 4, 80, -1)

# Convert the tuple to a timestamp
timestamp = time.mktime(time_tuple)

# Convert the timestamp to a struct_time object
struct_time = time.localtime(timestamp)

print(struct_time)

dt1 = datetime.datetime.now()
dt2 = datetime.datetime(2022, 1, 2, 11, 1, 4)
dt3 = datetime.datetime(2023, 10, 1, 12, 0, 0, 123456)

datetime.datetime.today() # type: ignore
datetime.datetime.now() # type: ignore

dt4 = datetime.datetime(
    year=2023, 
    month=10, 
    day=1, 
    hour=12, 
    minute=0, 
    second=0, 
    microsecond=123456, 
    tzinfo=datetime.timezone.utc
)

t1 = datetime.time(23, 59, 59)
t2 = datetime.time(22, 59, 59, 123456)
t1 > t2 # type: ignore
t1 == t2 # type: ignore

c = calendar.Calendar()
print(c.monthdayscalendar(2023, 10))
for day in c.itermonthdays4(2023, 10):
    print(day)

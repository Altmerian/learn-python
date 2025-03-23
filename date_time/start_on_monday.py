import datetime
import calendar


monday_count = 0

year = int(input("Enter a year: "))

for month in range(1, 13):
    first_day = datetime.date(year, month, 1)

    if first_day.weekday() == 0:
        monday_count += 1


print(f"In {year}, {monday_count} months start with a Monday.")

cal = calendar.TextCalendar()

print("\n2025 Calendar:")
print(cal.formatyear(2025))

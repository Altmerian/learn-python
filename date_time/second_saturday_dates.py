import calendar


def second_saturday_dates(year: int):
    second_saturdays = {}
    for month in range(1, 13):
        month_name = calendar.month_name[month]
        month_calendar = calendar.monthcalendar(year, month)
        sats = [w[calendar.SATURDAY] for w in month_calendar if w[calendar.SATURDAY] != 0]
        second_saturdays[month_name] = sats[1] if len(sats) >= 2 else None
    return second_saturdays

if __name__ == "__main__":
    print(second_saturday_dates(2025))

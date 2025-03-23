from datetime import date, timedelta


def all_sundays(year):
    """
    Returns a number of all Sundays in the given year.
    :param year: Year to check
    :return: Number of Sundays in the year
    """

    # Start from January 1st of the given year
    start_date = date(year, 1, 1)
    
    # Find the first Sunday of the year
    first_sunday = start_date + timedelta(days=(6 - start_date.weekday()))

    # Count Sundays in the year
    count = 0
    current_date = first_sunday
    while current_date.year == year:
        count += 1
        current_date += timedelta(weeks=1)

    return count

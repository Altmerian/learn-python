from datetime import datetime, timedelta


def get_last_weekday_date(day_of_week):
    """
    Return the most recent date for the given day of the week.

    Args:
        day_of_week (str or int): Day of the week. If string, can be full name ('Monday')
                                 or abbreviated ('Mon'). If integer, 0=Monday, 6=Sunday.

    Returns:
        datetime.date: The most recent date for the given day of the week.
    """
    # Define mapping for day names to integers (0=Monday, 6=Sunday)
    days = {
        "monday": 0,
        "mon": 0,
        "tuesday": 1,
        "tue": 1,
        "wednesday": 2,
        "wed": 2,
        "thursday": 3,
        "thu": 3,
        "friday": 4,
        "fri": 4,
        "saturday": 5,
        "sat": 5,
        "sunday": 6,
        "sun": 6,
    }

    # Try to convert input to integer if it's a digit string
    if isinstance(day_of_week, str) and day_of_week.isdigit():
        day_of_week = int(day_of_week)

    # Convert string day to integer if needed
    if isinstance(day_of_week, str):
        day = days.get(day_of_week.lower())
        if day is None:
            raise ValueError(f"Invalid day of week: {day_of_week}")
    else:
        day = day_of_week
        if not 0 <= day <= 6:
            raise ValueError("Day of week must be between 0 (Monday) and 6 (Sunday)")

    # Get today's date
    today = datetime.now().date()
    today_weekday = today.weekday()  # 0=Monday, 6=Sunday

    # Calculate days to go back
    if today_weekday >= day:
        days_diff = today_weekday - day
    else:
        days_diff = today_weekday + 7 - day

    return today - timedelta(days=days_diff)


if __name__ == "__main__":
    day_of_week = input("Enter the day of the week (e.g., 0-6, 'Monday' or 'Mon'): ")
    try:
        last_weekday_date = get_last_weekday_date(day_of_week)
        print(f"The most recent {day_of_week} was on: {last_weekday_date}")
    except ValueError as e:
        print(e)

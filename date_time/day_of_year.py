from datetime import datetime
import re


def day_of_year(date: str) -> int:
    """Calculate the day of the year for a given date.

    This function takes a date string in DD/MM/YYYY format and returns
    the corresponding day of the year (1-366). The function validates both
    the format and the date validity (including leap years).

    Args:
        date (str): The date string in DD/MM/YYYY format (e.g., "01/01/2025")

    Returns:
        int: The day of the year, ranging from 1 to 366 (for leap years)

    Raises:
        ValueError: If the date string is not in DD/MM/YYYY format or
                  if the date is invalid (e.g., "31/04/2025" or "29/02/2025" in non-leap year)

    Examples:
        >>> day_of_year("01/01/2025")
        1
        >>> day_of_year("31/12/2025")
        365
        >>> day_of_year("29/02/2024")  # Leap year
        60
    """
    # Check exact format with regex before attempting to parse
    if not re.match(r'^\d{2}/\d{2}/\d{4}$', date):
        raise ValueError("Invalid date format. Date must be in DD/MM/YYYY format")
        
    try:
        # Parse the date string into a datetime object
        date_obj = datetime.strptime(date, "%d/%m/%Y")
        
        # Get the day of the year
        return date_obj.timetuple().tm_yday
    except ValueError:
        raise ValueError("Invalid date format. Date must be in DD/MM/YYYY format")

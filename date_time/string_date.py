from datetime import date

def parse_date(date_str):
    # Split the input into a list
    date_parts = date_str.split("-")

    # Ensure we have exactly 3 parts
    if len(date_parts) != 3:
        raise ValueError("Input must be in the format DD-MM-YYYY")

    day_str, month_str, year_str = date_parts

    # Check format compliance
    if not (len(day_str) == 2 and day_str.isdigit()):
        raise ValueError("Day must be two digits (e.g., 01)")

    if not (len(month_str) == 2 and month_str.isdigit()):
        raise ValueError("Month must be two digits (e.g., 01)")

    if not (len(year_str) == 4 and year_str.isdigit()):
        raise ValueError("Year must be four digits (e.g., 2023)")

    return date(int(year_str), int(month_str), int(day_str))

if __name__ == "__main__":
    try:
        # Get user input
        date_str = input("Enter a date in DD-MM-YYYY format (e.g., 01-01-2023): ")

        # Parse the date
        date_obj = parse_date(date_str)

        # Print results
        print(f"Date object: {date_obj}")

    except ValueError as e:
        print(f"Error: Invalid date format or values. {e}")

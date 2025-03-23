from datetime import date


def calculate_age(birth_date):
    today = date.today()

    age = today.year - birth_date.year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
    return age


if __name__ == "__main__":
    # Example usage
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    year, month, day = map(int, birth_date_str.split("-"))
    birth_date = date(year, month, day)

    age = calculate_age(birth_date)
    print(f"Your age is: {age} years")

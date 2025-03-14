class NegativeAgeException(Exception):
    pass


def stage(age):
    if age < 0:
        raise NegativeAgeException("Age cannot be negative")
    elif 0 <= age < 13:
        return "Kid"
    elif 13 <= age < 19:
        return "Teen"
    elif 19 <= age < 50:
        return "Young"
    else:
        return "Old"


if __name__ == "__main__":
    try:
        age = int(input("Enter your age: "))
        print(stage(age))
    except NegativeAgeException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")

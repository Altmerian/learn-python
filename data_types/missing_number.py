from array import array


def find_missing_number(numbers: array) -> int:
    missing_number = sum(range(numbers[0], numbers[-1] + 1)) - sum(numbers)
    return missing_number if missing_number != 0 else -1


if __name__ == "__main__":
    numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 10])
    print(f"Missing number: {find_missing_number(numbers)}")
    numbers = array("i", [11, 12, 13, 14, 16, 17, 18, 19, 20])
    print(f"Missing number: {find_missing_number(numbers)}")
    numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(f"Missing number: {find_missing_number(numbers)}")

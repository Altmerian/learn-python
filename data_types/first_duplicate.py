from array import array


def find_first_duplicate(numbers: array) -> int:
    seen = set()
    for n in numbers:
        if n in seen:
            return n
        seen.add(n)
    return -1


if __name__ == "__main__":
    numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 1, 3, 4, 5])
    print(find_first_duplicate(numbers))  # Output: 2
    numbers = array("i", [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(find_first_duplicate(numbers))  # Output: -1

import bisect
from typing import Any


def insertion_sort(elements: list[Any]) -> list[Any]:
    result = []
    for i in range(1, len(elements)):
        key = elements[i]
        bisect.insort(result, key)
    return result


if __name__ == "__main__":
    elements = [9, 3, 7, 1, 5, 10, 8, 4, 6]
    print(insertion_sort(elements))

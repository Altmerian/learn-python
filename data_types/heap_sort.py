import heapq
from array import array
from typing import Any


def heap_sort(elements):
    elements_copy = elements.copy()
    heapq.heapify(elements_copy)
    return [heapq.heappop(elements_copy) for _ in range(len(elements_copy))]


def heap_sort_array(arr: array[Any]) -> array[Any]:
    elements = list(arr)
    return array(arr.typecode, heap_sort(elements))


if __name__ == "__main__":
    elements = [9, 3, 7, 1, 5, 10, 8, 4, 6]
    print(heap_sort(elements))

    arr = array("i", [4, 5, 2, 1, 54, 34, 2, -2])
    print(heap_sort_array(arr).tolist())

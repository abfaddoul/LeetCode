import heapq
from typing import List


def make_heap(numbers: List[int]) -> List[int]:
    heapq.heapify(numbers)
    return numbers


def get_min(numbers: List[int]) -> int:
    heapq.heapify(numbers)
    return numbers[0]


def heapify_and_pop(numbers: List[int]) -> int:
    heapq.heapify(numbers)
    return heapq.heappop(numbers)


# do not modify below this line
print(make_heap([5, 2, 8, 1, 3]))
print(make_heap([10, 4, 7, 2, 8]))

print(get_min([5, 2, 8, 1, 3]))
print(get_min([10, 4, 7, 2, 8]))

print(heapify_and_pop([5, 2, 8, 1, 3]))
print(heapify_and_pop([10, 4, 7, 2, 8]))

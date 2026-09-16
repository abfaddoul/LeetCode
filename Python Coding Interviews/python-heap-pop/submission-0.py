import heapq
from typing import List


def pop_min(heap: List[int]) -> int:
    return heapq.heappop(heap)


def pop_two(heap: List[int]) -> List[int]:
    heapq.heappop(heap)
    heapq.heappop(heap)
    return heap


def pop_and_get_next(heap: List[int]) -> int:
    heapq.heappop(heap)
    return heap[0]


# do not modify below this line
print(pop_min([1, 3, 2, 7, 5]))
print(pop_min([2, 4, 3, 8, 6]))

print(pop_two([1, 2, 3, 4, 5]))
print(pop_two([2, 3, 5, 7, 6]))

print(pop_and_get_next([1, 3, 2, 7, 5]))
print(pop_and_get_next([2, 4, 3, 8, 6]))

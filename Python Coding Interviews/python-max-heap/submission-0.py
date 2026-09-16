import heapq
from typing import List


def push_max(heap: List[int], value: int) -> List[int]:
    heapq.heappush(heap, -value)
    return heap


def get_max(heap: List[int]) -> int:
    return -heap[0]


def pop_max(heap: List[int]) -> int:
    return -heapq.heappop(heap)


# do not modify below this line
print(push_max([-8, -2, -5], 10))
print(push_max([-7, -3, -4], 6))

print(get_max([-8, -2, -5]))
print(get_max([-10, -4, -6]))

print(pop_max([-8, -2, -5]))
print(pop_max([-10, -4, -6]))

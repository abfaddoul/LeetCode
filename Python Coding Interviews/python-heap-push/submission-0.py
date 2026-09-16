import heapq
from typing import List


def push_value(heap: List[int], value: int) -> List[int]:
    heapq.heappush(heap, value)
    return heap


def push_two(heap: List[int], a: int, b: int) -> List[int]:
    heapq.heappush(heap, a)
    heapq.heappush(heap, b)
    return heap


def push_and_get_min(heap: List[int], value: int) -> int:
    heapq.heappush(heap, value)
    return heap[0]


# do not modify below this line
print(push_value([2, 5, 8], 1))
print(push_value([3, 7, 9], 4))

print(push_two([2, 5], 1, 8))
print(push_two([4, 6], 3, 10))

print(push_and_get_min([2, 5, 8], 1))
print(push_and_get_min([3, 7, 9], 4))

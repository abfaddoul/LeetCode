from sortedcontainers import SortedSet
from typing import List


def create_sorted_set(numbers: List[int]) -> SortedSet:
    pass


def get_smallest(numbers: List[int]) -> int:
    pass


def add_value(
    numbers: List[int],
    value: int
) -> SortedSet:
    pass


# do not modify below this line
print(create_sorted_set([5, 2, 8, 2, 1]))
print(create_sorted_set([10, 4, 7, 4, 6]))

print(get_smallest([5, 9, 2, 7]))
print(get_smallest([12, 3, 8, 4]))

print(add_value([5, 2, 8], 1))
print(add_value([10, 4, 7], 6))

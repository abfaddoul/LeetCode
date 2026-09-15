from typing import List


def create_set(numbers: List[int]) -> set[int]:
    return set(numbers)


def contains_value(numbers: List[int], target: int) -> bool:
    numbers = set(numbers)
    return target in numbers 


def add_value(numbers: set[int], value: int) -> set[int]:
    numbers.add(value)
    return numbers


# do not modify below this line
print(create_set([1, 2, 2, 3, 3, 3]))
print(create_set([5, 5, 6, 7]))

print(contains_value([1, 2, 3], 2))
print(contains_value([1, 2, 3], 5))

print(add_value({1, 2}, 3))
print(add_value({5, 6}, 5))

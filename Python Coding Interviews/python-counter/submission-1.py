from collections import Counter
from typing import List


def count_numbers(numbers: List[int]) -> dict[int, int]:
    return Counter(numbers)


def get_count(numbers: List[int], target: int) -> int:
    count = Counter(numbers)
    return count[target]


def most_common_number(numbers: List[int]) -> int:
    count = Counter(numbers)
    return count.most_common(1)[0][0]


# do not modify below this line
print(count_numbers([1, 2, 1, 3, 2, 1]))
print(count_numbers([5, 5, 2, 5]))

print(get_count([1, 2, 1, 3, 1], 1))
print(get_count([1, 2, 3], 5))

print(most_common_number([1, 2, 1, 3, 1]))
print(most_common_number([4, 4, 2, 3, 4, 2]))

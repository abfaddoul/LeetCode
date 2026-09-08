from typing import List, Tuple


def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    return min(numbers), max(numbers)


def limit_score(score: int) -> int:
    return min(max(score, 0), 100)


# do not modify below this line
print(get_min_max([5, 2, 8, 1, 4]))
print(get_min_max([10, -5, 3, 20, 7]))

print(limit_score(75))
print(limit_score(120))
print(limit_score(-20))
print(limit_score(100))

from collections import defaultdict
from typing import List


def count_numbers(numbers: List[int]) -> dict[int, int]:
    count = defaultdict(int)
    for num in numbers:
        count[num] += 1
    return count


def group_words(words: List[str]) -> dict[str, List[str]]:
    group = defaultdict(list)
    for word in words:
        group[word[0]] += [word]
    return group


def get_count(numbers: List[int], target: int) -> int:
    count = defaultdict(int)
    for num in numbers:
        count[num] += 1
    return count[target]


# do not modify below this line
print(count_numbers([1, 2, 1, 3, 2, 1]))
print(count_numbers([5, 5, 5, 2]))

print(group_words(["apple", "ant", "banana", "blue"]))
print(group_words(["cat", "car", "dog", "door"]))

print(get_count([1, 2, 1, 3, 1], 1))
print(get_count([1, 2, 3], 5))

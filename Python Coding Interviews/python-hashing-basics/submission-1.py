from typing import List


def get_hash(value: str) -> int:
    return hash(value)


def has_duplicate(numbers: List[int]) -> bool:
    return len(numbers) != len(set(numbers))


def count_values(numbers: List[int]) -> dict[int, int]:
    count = {}

    for num in numbers:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1

    return count


# do not modify below this line
print(get_hash("apple"))
print(get_hash("hello"))

print(has_duplicate([1, 2, 3, 1]))
print(has_duplicate([1, 2, 3, 4]))

print(count_values([1, 2, 1, 3, 2, 1]))
print(count_values([5, 5, 2, 8]))

from typing import List


def append_elements(numbers: List[int], a: int, b: int) -> List[int]:
    numbers.append(a)
    numbers.append(b)
    return numbers


def remove_last_two(numbers: List[int]) -> List[int]:
    numbers.pop()
    numbers.pop()
    return numbers


def get_last(numbers: List[int]) -> int:
    last = numbers.pop()
    return last


# do not modify below this line
print(append_elements([1, 2, 3], 4, 5))
print(append_elements([10], 20, 30))

print(remove_last_two([1, 2, 3, 4]))
print(remove_last_two([5, 6, 7]))

print(get_last([1, 2, 3]))
print(get_last([10, 20, 30, 40]))

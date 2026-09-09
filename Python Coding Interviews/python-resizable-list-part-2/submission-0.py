from typing import List


def insert_middle(numbers: List[int], value: int) -> List[int]:
    numbers.insert(1,value)
    return numbers


def remove_second(numbers: List[int]) -> List[int]:
    numbers.pop(1)
    return numbers


def remove_at(numbers: List[int], index: int) -> int:
    return numbers.pop(index)


# do not modify below this line
print(insert_middle([1, 3, 4], 2))
print(insert_middle([10, 30], 20))

print(remove_second([1, 2, 3, 4]))
print(remove_second([10, 20, 30]))

print(remove_at([5, 10, 15], 1))
print(remove_at([7, 8, 9, 10], 2))

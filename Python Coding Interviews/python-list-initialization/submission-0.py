from typing import List


def create_zeros(n: int) -> List[int]:
    return [0] * n


def create_values(n: int, value: int) -> List[int]:
    return [value] * n


def create_sequence(n: int) -> List[int]:
    return [i for i in range(n)]


# do not modify below this line
print(create_zeros(5))
print(create_zeros(3))

print(create_values(4, 7))
print(create_values(3, -1))

print(create_sequence(5))
print(create_sequence(3))

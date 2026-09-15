from typing import List


def unique_values(numbers: List[int]) -> set[int]:
    return {n for n in numbers}


def create_squares(n: int) -> set[int]:
    return {i*i for i in range(n)}


def get_even_numbers(numbers: List[int]) -> set[int]:
    return {n for n in numbers if n % 2 == 0}


# do not modify below this line
print(unique_values([1, 2, 2, 3, 3, 3]))
print(unique_values([5, 5, 6, 7]))

print(create_squares(5))
print(create_squares(3))

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers([7, 8, 9, 10]))

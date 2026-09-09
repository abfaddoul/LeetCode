from typing import List


def double_numbers(numbers: List[int]) -> List[int]:
    return [n * 2 for n in numbers]


def get_even_numbers(numbers: List[int]) -> List[int]:
    return [n for n in numbers if n % 2 == 0]


def create_squares(n: int) -> List[int]:
    return [i * i for i in range(n)]


# do not modify below this line
print(double_numbers([1, 2, 3, 4]))
print(double_numbers([5, 10, 15]))

print(get_even_numbers([1, 2, 3, 4, 5, 6]))
print(get_even_numbers([7, 8, 9, 10]))

print(create_squares(5))
print(create_squares(3))

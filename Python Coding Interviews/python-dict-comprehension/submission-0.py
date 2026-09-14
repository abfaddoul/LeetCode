from typing import List


def create_squares(n: int) -> dict[int, int]:
    return {i: i * i for i in range(n)}


def word_lengths(words: List[str]) -> dict[str, int]:
    return {word: len(word) for word in words}


def even_squares(numbers: List[int]) -> dict[int, int]:
    return {number: number * number for number in numbers if number % 2 == 0}


# do not modify below this line
print(create_squares(5))
print(create_squares(3))

print(word_lengths(["apple", "cat", "banana"]))
print(word_lengths(["hi", "hello"]))

print(even_squares([1, 2, 3, 4, 5, 6]))
print(even_squares([7, 8, 9, 10]))

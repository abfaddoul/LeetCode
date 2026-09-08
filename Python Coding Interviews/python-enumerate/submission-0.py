from typing import List


def add_index(numbers: List[int]) -> List[int]:
    res = []
    for i, number in enumerate(numbers):
        res.append(i+number)
    return res


def find_word(words: List[str], target: str) -> int:
    j = -1
    for i, word in enumerate(words):
        if word == target:
            j = i
    return j


# do not modify below this line
print(add_index([5, 5, 5]))
print(add_index([10, 20, 30, 40]))

print(find_word(["apple", "banana", "orange"], "banana"))
print(find_word(["cat", "dog", "bird"], "bird"))
print(find_word(["red", "green", "blue"], "yellow"))

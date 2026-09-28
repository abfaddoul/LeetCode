from typing import List


def reverse_list(numbers: List[int]) -> List[int]:
    left, right = 0, len(numbers) - 1
    while left < right:
        temp = numbers[right]
        numbers[right] = numbers[left]
        numbers[left] = temp
        left += 1
        right -= 1
    return numbers


def is_palindrome(word: str) -> bool:
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left += 1
        right -= 1
    return True


def sum_from_ends(numbers: List[int]) -> List[int]:
    left, right = 0, len(numbers) - 1
    res = []

    while left <= right:
        if left == right:
            res.append(numbers[left])
        else:
            res.append(numbers[left] + numbers[right])

        left += 1
        right -= 1

    return res


# do not modify below this line
print(reverse_list([1, 2, 3, 4]))
print(reverse_list([5, 10, 15]))

print(is_palindrome("racecar"))
print(is_palindrome("hello"))

print(sum_from_ends([1, 2, 3, 4]))
print(sum_from_ends([2, 5, 8, 10, 20, 30]))

from typing import List


def max_window_sum(numbers: List[int], k: int) -> int:
    window_sum = sum(numbers[:k])
    mx = window_sum

    for right in range(k, len(numbers)):
        window_sum -= numbers[right - k]
        window_sum += numbers[right]
        mx = max(mx, window_sum)

    return mx


def min_window_sum(numbers: List[int], k: int) -> int:
    window_sum = sum(numbers[:k])
    mn = window_sum

    for right in range(k, len(numbers)):
        window_sum -= numbers[right - k]
        window_sum += numbers[right]
        mn = min(mn, window_sum)

    return mn


def window_sums(numbers: List[int], k: int) -> List[int]:
    window_sum = sum(numbers[:k])
    res = [window_sum]

    for right in range(k, len(numbers)):
        window_sum -= numbers[right - k]
        window_sum += numbers[right]
        res.append(window_sum)

    return res


# do not modify below this line
print(max_window_sum([1, 2, 3, 4, 5], 3))
print(max_window_sum([5, 1, 2, 10, 3], 2))

print(min_window_sum([1, 2, 3, 4, 5], 3))
print(min_window_sum([5, 1, 2, 10, 3], 2))

print(window_sums([1, 2, 3, 4, 5], 3))
print(window_sums([5, 1, 2, 10, 3], 2))

def in_range(n: int, low: int, high: int) -> bool:
    return low <= n <= high


def is_increasing(a: int, b: int, c: int) -> bool:
    return a < b < c


# do not modify below this line
print(in_range(5, 1, 10))
print(in_range(1, 1, 10))
print(in_range(15, 1, 10))

print(is_increasing(1, 2, 3))
print(is_increasing(1, 1, 3))
print(is_increasing(5, 3, 1))

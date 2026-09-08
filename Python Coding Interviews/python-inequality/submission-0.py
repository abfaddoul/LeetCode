def in_range(n: int, low: int, high: int) -> bool:
    if low <= n <= high:
        return True
    return False


def is_increasing(a: int, b: int, c: int) -> bool:
    if a < b < c:
        return True
    return False


# do not modify below this line
print(in_range(5, 1, 10))
print(in_range(1, 1, 10))
print(in_range(15, 1, 10))

print(is_increasing(1, 2, 3))
print(is_increasing(1, 1, 3))
print(is_increasing(5, 3, 1))

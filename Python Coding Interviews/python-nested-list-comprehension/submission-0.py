from typing import List


def create_grid(rows: int, cols: int) -> List[List[int]]:
    return [[0 for _ in range(cols)] for _ in range(rows)]


def create_value_grid(
    rows: int,
    cols: int,
    value: int
) -> List[List[int]]:
    return [[value for _ in range(cols)] for _ in range(rows)]


def create_index_grid(rows: int, cols: int) -> List[List[int]]:
    return [[r + c for c in range(cols)] for r in range(rows)]


# do not modify below this line
print(create_grid(2, 3))
print(create_grid(3, 2))

print(create_value_grid(2, 3, 5))
print(create_value_grid(3, 2, -1))

print(create_index_grid(2, 3))
print(create_index_grid(3, 2))

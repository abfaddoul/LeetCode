from typing import List


def count_rows(grid: List[List[int]]) -> int:
    return len(grid)


def count_cols(grid: List[List[int]]) -> int:
    return len(grid[0])


def sum_diagonal(grid: List[List[int]]) -> int:
    total = 0

    for i in range(len(grid)):
        total += grid[i][i]

    return total


# do not modify below this line
print(count_rows([[1, 2, 3], [4, 5, 6]]))
print(count_rows([[1], [2], [3], [4]]))

print(count_cols([[1, 2, 3], [4, 5, 6]]))
print(count_cols([[1, 2], [3, 4], [5, 6]]))

print(sum_diagonal([[1, 2], [3, 4]]))
print(sum_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

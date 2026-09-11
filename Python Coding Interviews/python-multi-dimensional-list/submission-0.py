from typing import List


def get_value(
    matrix: List[List[int]],
    row: int,
    col: int
) -> int:
        return matrix[row][col]



def set_value(
    matrix: List[List[int]],
    row: int,
    col: int,
    value: int
) -> List[List[int]]:
    matrix[row][col] = value
    return matrix

def sum_all(matrix: List[List[int]]) -> int:
    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            k += matrix[i][j]

    return k


# do not modify below this line
matrix1 = [
    [1, 2],
    [3, 4]
]

print(get_value(matrix1, 0, 1))
print(get_value(matrix1, 1, 0))

matrix2 = [
    [1, 2],
    [3, 4]
]

print(set_value(matrix2, 0, 1, 10))
print(set_value(matrix2, 1, 0, 20))

print(sum_all([[1, 2], [3, 4]]))
print(sum_all([[5, 5, 5], [1, 2, 3]]))

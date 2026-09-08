from typing import List, Tuple


def sum_pairs(pairs: List[Tuple[int, int]]) -> List[int]:
    res = []
    for x, y in pairs:
        res.append(x+y)
    return res


def compute_areas(rectangles: List[Tuple[int, int]]) -> List[int]:
    res = []
    for h, w in rectangles:
        res.append(h*w)
    return res


# do not modify below this line
print(sum_pairs([(1, 2), (3, 4), (5, 6)]))
print(sum_pairs([(10, 5), (2, 8), (7, 3)]))

print(compute_areas([(2, 3), (4, 5), (6, 2)]))
print(compute_areas([(1, 7), (3, 3), (10, 4)]))

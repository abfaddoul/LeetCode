from typing import List


def add_lists(list1: List[int], list2: List[int]) -> List[int]:
    res = []
    for l1, l2 in zip(list1, list2):
        res.append(l1 + l2)
    return res


def match_names_scores(names: List[str], scores: List[int]) -> List[str]:
    res = []
    for name, score in zip(names, scores):
        res.append(f"{name}: {score}")
    return res


# do not modify below this line
print(add_lists([1, 2, 3], [4, 5, 6]))
print(add_lists([10, 20, 30], [1, 2, 3]))

print(match_names_scores(["Alice", "Bob", "Charlie"], [90, 80, 85]))
print(match_names_scores(["John", "Jane"], [100, 95]))

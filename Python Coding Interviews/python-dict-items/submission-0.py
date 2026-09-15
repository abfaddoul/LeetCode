from typing import List


def print_pairs(data: dict[str, int]) -> List[str]:
    res = []
    for key, value in data.items():
        res.append(f"{key}:{value}")
    return res


def find_key(data: dict[str, int], target: int) -> str:
    for key, value in data.items():
        if value == target:
            return key
    return ""


def sum_values(data: dict[str, int]) -> int:
    sm = 0
    for value in data.values():
        sm += value
    return sm 


# do not modify below this line
print(print_pairs({"a": 1, "b": 2}))
print(print_pairs({"x": 10, "y": 20}))

print(find_key({"a": 1, "b": 2, "c": 3}, 2))
print(find_key({"x": 10, "y": 20}, 20))

print(sum_values({"a": 1, "b": 2, "c": 3}))
print(sum_values({"x": 10, "y": 20}))

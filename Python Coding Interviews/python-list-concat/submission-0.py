from typing import List


def combine_lists(list1: List[int], list2: List[int]) -> List[int]:
    return list1 + list2


def combine_three(
    list1: List[str],
    list2: List[str],
    list3: List[str]
) -> List[str]:
    return list1 + list2 + list3


# do not modify below this line
print(combine_lists([1, 2, 3], [4, 5, 6]))
print(combine_lists([10, 20], [30, 40]))

print(combine_three(["a", "b"], ["c"], ["d", "e"]))
print(combine_three(["apple"], ["banana", "orange"], ["pear"]))

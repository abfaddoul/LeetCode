from typing import List


def clone_list(numbers: List[int]) -> List[int]:
    copy = numbers[:]
    return copy


def clone_and_add(numbers: List[int], value: int) -> List[int]:
    copy = numbers.copy()
    copy.append(value)
    return copy


# do not modify below this line
nums1 = [1, 2, 3]
print(clone_list(nums1))
print(nums1)

nums2 = [10, 20]
print(clone_and_add(nums2, 30))
print(nums2)

nums3 = [5, 6, 7]
print(clone_and_add(nums3, 8))
print(nums3)

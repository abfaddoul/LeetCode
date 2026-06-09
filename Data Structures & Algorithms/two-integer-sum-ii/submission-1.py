class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        ln = len(numbers)
        lst = []
        while left < ln:
            right = left + 1
            while right < ln:
                if numbers[left] != numbers[right]:
                    if numbers[left] + numbers[right] == target:
                        lst.append(left + 1)
                        lst.append(right + 1)
                        return lst
                right += 1
            left += 1
        return lst

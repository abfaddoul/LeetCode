class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        i = 0
        while i < len(nums):
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    return True
                j = j + 1
            i = i + 1
        return False
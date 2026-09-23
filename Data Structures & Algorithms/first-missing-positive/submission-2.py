class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mn = 1
        while mn in nums:
            mn += 1
        return mn
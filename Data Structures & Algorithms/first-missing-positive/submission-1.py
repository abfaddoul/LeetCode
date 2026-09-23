class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        mn = 1
        # while 0 in nums:
        #     nums.remove(0)
        # for num in nums:
        #     if abs(num) < mn:
        #         mn = abs(num)
        while mn in nums:
            mn += 1
        return mn
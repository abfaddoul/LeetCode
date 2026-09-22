class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        temp = 1
        mx = 1

        for i in range(1, len(nums)):
            if nums[i - 1] + 1 == nums[i]:
                temp += 1
            else :
                temp = 1
            mx = max(temp, mx)
        return mx
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        if not nums:
            return 0
        count = 1
        mx = 1

        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                count += 1
            else:
                count = 1
            
            mx = max(mx, count)

        return mx
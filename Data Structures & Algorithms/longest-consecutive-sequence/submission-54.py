class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(set(nums))
        mx = 1
        count = 1

        if  not nums:
            return 0

        for i in range(len(nums) - 1):

            if nums[i] + 1 == nums[i + 1]:
                count += 1

            else:
                count = 1

            if count > mx:
                mx = count

        return mx
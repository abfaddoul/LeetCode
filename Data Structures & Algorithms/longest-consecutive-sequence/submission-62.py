class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        mx = 0
        nums = set(nums)

        for num in nums:
            if  num - 1 not in nums:
                curr = num
                count = 1
                while curr + 1 in nums:
                    count += 1
                    curr += 1
                mx = max(mx, count)     
        return mx
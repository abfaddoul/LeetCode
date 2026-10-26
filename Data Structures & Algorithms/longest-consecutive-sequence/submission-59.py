class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 1
        if not nums:
            return 0

        for num in nums:
            count = 1                        
            if num - 1 not in nums:
                curr = num
                while curr + 1 in nums:
                    count += 1
                    curr += 1
                m = max(m, count)
        return m
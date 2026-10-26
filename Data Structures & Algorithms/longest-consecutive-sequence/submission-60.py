class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        m = 1
        if not nums:
            return 0

        for num in nums:
            if num - 1 not in nums:
                count = 1                        
                curr = num
                while curr + 1 in nums:
                    count += 1
                    curr += 1
                m = max(m, count)
        return m

        # time complexity : o(n)
        # space complexity : o(n)
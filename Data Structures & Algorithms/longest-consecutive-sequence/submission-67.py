class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m = 0
        numset = set(nums)

        for num in numset :
            if num - 1 not in numset:
                count = 1
                while num + count in numset:
                    count += 1
                m = max(m, count)
        return m
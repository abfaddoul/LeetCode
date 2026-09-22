class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        n_set = set(nums)
        n = 1
        mx = 1

        for num in n_set:
            if num - 1 not in n_set:
                current = num
                while current + 1 in n_set:
                    n += 1
                    current += 1
                mx = max(n, mx)
            else:
                n = 1
        return mx

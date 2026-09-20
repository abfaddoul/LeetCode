class Solution:
    def subsetXORSum(self, nums: list[int]) -> int:

        def dfs(i, current):
            if i == len(nums):
                return current

            skip = dfs(i + 1, current)

            take = dfs(i + 1, current ^ nums[i])

            return skip + take

        return dfs(0, 0)
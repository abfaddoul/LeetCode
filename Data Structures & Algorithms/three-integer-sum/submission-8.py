class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        trp =  []
        nums.sort()
        i = 0
        while i < len(nums) - 2:
            j = i + 1
            k = len(nums) - 1
            while j < k:
                if  nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    trp = [nums[i]] + [nums[j]] + [nums[k]]
                    if trp not in res:
                        res.append(trp)
                    j += 1
                    k -= 1
            i += 1
        return res

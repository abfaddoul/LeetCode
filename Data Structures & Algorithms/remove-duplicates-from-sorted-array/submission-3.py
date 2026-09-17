class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        temp = sorted(list(set(nums)))
        k = len(temp)

        for i in range(k):
            nums[i] = temp[i]

        return k
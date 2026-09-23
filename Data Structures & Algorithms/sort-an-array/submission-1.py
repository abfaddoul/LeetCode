class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            mn = float('inf')
            for num in nums:
                if num < mn:
                    mn = num
            res.append(mn)
            nums.remove(mn)
        return res
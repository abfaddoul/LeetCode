class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums) / 2
        res = defaultdict(int)
        for num in nums:
            res[num] += 1
        for key, value in res.items():
            if value > n:
                return key
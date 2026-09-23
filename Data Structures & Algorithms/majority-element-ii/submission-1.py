class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct = defaultdict(int)
        res = []

        for num in nums:
            dct[num] += 1

        for key, value in dct.items():
            if value > len(nums) / 3:
                res.append(key)
        return res        
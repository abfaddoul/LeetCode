class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        dct, res, n = defaultdict(int), [], len(nums)

        for num in nums:
            dct[num] += 1
        print(dct)
        for key, value in dct.items():
            if value > n / 3:
                res.append(key)
        return res        
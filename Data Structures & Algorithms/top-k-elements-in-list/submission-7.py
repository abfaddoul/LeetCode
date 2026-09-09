class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        dct = {}

        for num in nums:
            if num in dct:
                dct[num] += 1
            else:
                dct[num] = 1

        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in dct.items():
            buckets[freq].append(num)

        for i in range(len(nums), 0, -1):
                for bucket in buckets[i]:
                    res.append(bucket)
                    if len(res) == k:
                        return res[::-1]
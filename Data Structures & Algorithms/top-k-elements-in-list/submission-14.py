class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        res = []

        for i in range(k):
            key = max(n, key=n.get)
            res.append(key)
            del n[key]

        return res
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = Counter(nums)
        res = []

        for i in range(k):
            key = max(h, key=h.get)
            res.append(key)
            del h[key]
        
        return res
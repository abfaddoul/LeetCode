class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        heap = []
        for num in nums:
            heapq.heappush(heap, num * num)
        return [heapq.heappop(heap) for _ in range(len(heap))]
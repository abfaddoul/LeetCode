from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []

        for r in range(len(nums)):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()

            q.append(r)

            if q[0] <= r - k:
                q.popleft()

            if r >= k - 1:
                res.append(nums[q[0]])

        return res
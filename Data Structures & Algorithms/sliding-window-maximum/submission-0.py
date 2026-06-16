class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, len(nums)
        out = []

        while l + k - 1 < r:
            curr = nums[l:l+k]
            out.append(max(curr))
            l += 1
        return out
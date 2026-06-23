class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, len(nums)
        out = []
        while l + k < r + 1:
            part = nums[l:l+k]
            out.append(max(part))
            l += 1
        return out           
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, len(nums) + 1
        out = []
        while l + k < r:
            part = nums[l:l+k]
            out.append(max(part))
            l += 1
        return out
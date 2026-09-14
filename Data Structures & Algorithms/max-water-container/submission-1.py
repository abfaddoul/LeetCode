class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r, xm = 0, len(heights) - 1, 0

        while l < r:
            m = (r - l) * abs(min(heights[l], heights[r]))
            if m > xm:
                xm = m
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                r -= 1
                l += 1
        return xm
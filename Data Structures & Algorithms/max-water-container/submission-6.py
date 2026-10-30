class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        left, right = 0, len(heights) - 1
        m = 0

        while left < right:
            cal = min(heights[right], heights[left]) * (right - left)
            if heights[right] < heights[left]:
                right -= 1
            elif heights[right] > heights[left]:
                left += 1
            else:
                left += 1
                right -= 1
            m = max(cal, m)
        return m

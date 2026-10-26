class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        mx = min(heights[right], heights[left]) * (right - left)

        while left < right:
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
            mx = max(mx, min(heights[right], heights[left]) * (right - left))
        return mx
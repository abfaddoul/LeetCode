class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        n = len(height) - 1
        count = 0

        while i < n and height[i] < height[i + 1]:
            i += 1
        while i < n and height[n] < height[n - 1]:
            n -= 1
    
        while i < n:
            j = i + 1
            while j < n and height[j] < height[i]:
                j+= 1
            
            if height[j] < height[i]:
                j = i + 1
                for k in range(i + 2, n + 1):
                    if height[k] > height[j]:
                        j = k

            sm = 0
            for k in range(i + 1, j):
                sm += height[k]

            count += min(height[i], height[j]) * (j - i - 1) - sm
            i = j
        return count

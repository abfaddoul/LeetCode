class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        if not heights:
            return 0
        i, j = 0, 0
        il, jl = len(heights), len(heights[0])
        heap, mx, visited = [[0, 0, 0]], 0, set()

        while heap:
            effort, i, j = heapq.heappop(heap)
            if (i,j) in visited:
                continue
            visited.add((i, j))

            if i == il - 1 and j == jl - 1:
                break

            if i < il -1:
                heapq.heappush(heap, (max(effort, abs(heights[i+1][j] - heights[i][j])), i + 1, j))
            if j < jl -1:
                heapq.heappush(heap, (max(effort, abs(heights[i][j + 1] - heights[i][j])), i, j + 1))
            if i > 0:
                heapq.heappush(heap, (max(effort, abs(heights[i-1][j] - heights[i][j])), i - 1, j))
            if j > 0:
                heapq.heappush(heap, (max(effort, abs(heights[i][j - 1] - heights[i][j])), i, j - 1))
        return effort
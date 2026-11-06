class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix) - 1, len(matrix[0])
        r, l = 0 , n - 1

        while r <= m and l >= 0:
            if matrix[r][l] < target:
                r += 1
            elif matrix[r][l] > target:
                l -= 1
            else :
                return True

        return False
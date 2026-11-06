class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        mh = 0

        while t <= b:
            mh = (t + b) // 2

            if matrix[mh][0] > target:
                b = mh - 1
            elif matrix[mh][-1] < target:
                t = mh + 1
            else:
                break
        if t > b:
            return False

        while l <= r:
            mw = (l + r) // 2
            
            if matrix[mh][mw] > target:
                r = mw - 1
            elif matrix[mh][mw] < target:
                l = mw + 1
            else:
                return True

        return False
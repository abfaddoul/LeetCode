class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        curr = 0
        l = len(arr)
        res = []
        while curr < l - 1:
            r = curr + 1
            g = r
            while r < l:
                if arr[r] > arr[g]:
                    g = r
                r += 1
            res.append(arr[g])
            curr += 1
        res.append(-1)
        return res
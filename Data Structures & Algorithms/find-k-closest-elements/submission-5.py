class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr.append(x)
        arr.sort()
        res = []
        for i in range(len(arr)):
            if arr[i] == x:
                break
        for j in range(k):
            if i + 1 < len(arr):
                if abs(arr[i - 1] - x) <= abs(arr[i + 1] - x):
                    temp = arr[i - 1]
                    res.append(arr[i - 1])
                    arr.remove(arr[i - 1])
                    i -= 1
                else:
                    temp = arr[i + 1]
                    res.append(arr[i + 1])
                    arr.remove(arr[i + 1])
            else :
                temp = arr[i - 1]
                res.append(arr[i - 1])
                arr.remove(arr[i - 1])
                i -= 1
        return sorted(res)
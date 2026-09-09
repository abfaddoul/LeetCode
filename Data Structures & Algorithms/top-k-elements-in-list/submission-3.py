class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        res = []
        dct = {}
        for num in nums:
            if num in dct:
                dct[num] += 1
            else :
                dct[num] = 1
                
        i = 0
        for i in range(k): 
            g = max(dct.values())
            if dct:
                for num, f in dct.items() :
                    if f == g:
                        res.append(num)
                        del dct[num]
                        break
        
        return res[::-1]
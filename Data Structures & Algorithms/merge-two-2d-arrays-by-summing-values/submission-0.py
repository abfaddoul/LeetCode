class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        hell = defaultdict(int)
        nums = sorted(nums1 + nums2)
        res = []

        for num in  nums:
            hell[num[0]] += num[1]
        print(hell)
        
        for k, v in hell.items():
            res.append([k,v])
        
        return res
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        h = defaultdict(list)

        for s in strs:
            h[str(sorted(list(s)))].append(s)
        
        for k, vs in h.items():
            temp = []
            for v in vs:
                temp.append(v)
            res.append(temp)
        return res
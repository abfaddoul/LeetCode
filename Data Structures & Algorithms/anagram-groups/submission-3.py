class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = defaultdict(list)

        for st in strs:
            d[str(sorted(list(st)))].append(st)
        
        return list(d.values()) 
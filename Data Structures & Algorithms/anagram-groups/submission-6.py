class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            d[str(sorted(list(s)))].append(s)
        
        return list(d.values())
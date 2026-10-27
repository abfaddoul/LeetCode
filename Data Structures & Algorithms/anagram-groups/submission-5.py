class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)

        for s in strs:
            d["".join(sorted(s))].append(s)
        
        return list(d.values())

        # Time Complexity : O(n × k log k)
        # Space Complexity : O(n × k)
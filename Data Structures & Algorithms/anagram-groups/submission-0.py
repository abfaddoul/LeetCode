class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}
        for word in strs:
            key = tuple(sorted(word))
            if key not in dct:
                dct[key] = []
            dct[key].append(word)
        return list(dct.values())


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i, j, sl, tl = 0, 0, len(s), len(t)
        while i < sl and j < tl:
            if s[i] == t[j]:
                i, j = i + 1, j + 1
            else :
                i += 1
        return tl - j
            

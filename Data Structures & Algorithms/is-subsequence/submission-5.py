class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False

        l, r, n = 0, 0, ""

        while l < len(s):
            if r < len(t) and s[l] == t[r]:
                n += s[l]
                l += 1
                r += 1
            else :
                r += 1
            if r == len(t) and n != s:
                return False
        if s == n:
            return True
        return False
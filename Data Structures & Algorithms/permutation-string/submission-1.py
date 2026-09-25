class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i, n = 0, len(s1) - 1
        while i + n < len(s2):
            if sorted(s1) == sorted(s2[i:i+n+1]):
                print(s2)
                return True
            i += 1
        return False


        # s1 = "ab"    s2 = "lecabee"  i = 0     n = 1   <   len(s2)  = 6
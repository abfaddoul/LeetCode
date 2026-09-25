class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i = 0
        n = len(s1)
        ss1 = sorted(s1)

        while i + n <= len(s2):

            if ss1 == sorted(s2[i:i + n]):
                return True

            i += 1
        
        return False
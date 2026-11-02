class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        s1 = sorted(list(s1))

        for i in range(len(s2)):
            per = sorted(s2[i:i+n])

            if per == s1:
                return True
        
        return False
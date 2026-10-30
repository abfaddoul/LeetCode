class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        perm = sorted(s1)
        for i in range(0,len(s2)):
            per = s2[i:i + n]
            print(per)
            if sorted(per) == perm:
                return True
        return False
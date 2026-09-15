class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "`" + str(len(s)) + "#" + s
        return res
    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        while i < len(s):
            re = ""
            g = ""
            if s[i]== "#":
                if s[i] and s[i-1].isnumeric():
                    p = i
                    while s[p-1].isnumeric() and p > 0:
                        g += s[p-1]
                        p -= 1
                    g = g[::-1]
                    l = int(g)
                    print(g)
                    if l > 0:
                        for j in range(l):
                            re += s[i+j+1]
                        i += j
                        res.append(re)
                    else :
                        res.append("")
            i += 1
        return res
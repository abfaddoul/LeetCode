class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s1 = ""

        for word in s:
            if word and s1:
                s1 += " "
            s1 += word[::-1]
        return s1
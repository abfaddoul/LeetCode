class Solution:
    def reverseString(self, s: List[str]) -> None:
        start = 0
        end = len(s) - 1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] =  temp
            start += 1
            end -= 1
        return s 
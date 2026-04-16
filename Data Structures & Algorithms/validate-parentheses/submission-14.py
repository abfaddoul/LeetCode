class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p = {"]":"[", "}":"{", ")":"("}
        i = 0
        while i < len(s):
            if s[i] in "[{(":
                stack.append(s[i])
            elif not stack or p[s[i]] != stack.pop():
                return False
            i += 1
        return not stack
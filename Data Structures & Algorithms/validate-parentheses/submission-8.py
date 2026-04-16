class Solution:
    def isValid(self, s: str) -> bool:
        if not "{" in s and not "[" in s and not "(" in s or len(s) % 2 != 0:
            return False
        stack = []
        p = {"]":"[", "}":"{", ")":"("}
        i = 0
        while i < len(s):
            if s[i] in "{[(":
                stack.append(s[i])
            else:
                if stack and p[s[i]] != stack.pop():
                    return  False
            i = i + 1
        return not stack
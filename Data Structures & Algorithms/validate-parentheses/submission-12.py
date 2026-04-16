class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"]":"[", "}":"{", ")":"("}
        for ch in s:
            if ch in "{[(":
                stack.append(ch)
            elif not stack or pairs[ch] != stack.pop():
                    return  False
        return not stack
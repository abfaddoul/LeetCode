class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def isin(s: str, pattern: str) -> bool:
            if len(s) % len(pattern) != 0:
                return False

            for i in range(0, len(s), len(pattern)):
                if s[i:i + len(pattern)] != pattern:
                    return False

            return True

        for i in range(min(len(str1), len(str2)), 0, -1):
            pattern = str2[:i]

            if isin(str1, pattern) and isin(str2, pattern):
                return pattern

        return ""
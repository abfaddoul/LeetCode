class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:
            while i < j and not s[i].isalnum():
                i = i + 1
            while j > i and not s[j].isalnum():
                j = j - 1
            if s[i] and s[j]:
                if s[i].lower() != s[j].lower():
                    return False
            i = i + 1
            j = j - 1
        return True
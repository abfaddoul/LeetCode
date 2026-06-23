class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        out = []
        while i < max(len(word1), len(word2)):
            if i < len(word1):
                out.append(word1[i])
            if i < len(word2):
                out.append(word2[i])
            i += 1
        output = "".join(out)
        return output
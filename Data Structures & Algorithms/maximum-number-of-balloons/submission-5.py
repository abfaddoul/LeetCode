class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        balloon = Counter("balloon")
        res = len(text)
        for c in balloon:
            res = min(res, count[c] // balloon[c])
        return res
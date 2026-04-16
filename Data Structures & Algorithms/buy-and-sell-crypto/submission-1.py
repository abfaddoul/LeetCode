class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        best = 0
        bestmn = 0
        bestmx = 0
        while i < len(prices) :
            j = i + 1
            while j < len(prices) :
                if prices[j] - prices[i] > best:
                    best =  prices[j] - prices[i]
                    bestmn = j
                    bestmx = i
                j = j + 1
            i = i + 1
        return best

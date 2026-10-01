class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        if len(prices) < 3:
            return money
        m = money - prices[0] - prices[1]
        if m >= 0:
            return m
        return money
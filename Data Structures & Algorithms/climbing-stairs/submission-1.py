class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        
        def dfs(n, memo):
            if n <= 2:
                return n
            if n in memo:
                return memo[n]
            memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
            return memo[n]

        return dfs(n, memo) 
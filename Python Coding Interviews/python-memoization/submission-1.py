def fibonacci(n: int) -> int:
    memo = {}

    def dfs(n, memo):
        if n <= 1:
            return n

        if n in memo:
            return memo[n]

        memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
        return memo[n]

    return dfs(n, memo)


def climb_stairs(n: int) -> int:
    memo = {}

    def dfs(n, memo):
        if n <= 2:
            return n
        
        if n in memo:
            return memo[n]
        
        memo[n] = dfs(n - 1, memo) + dfs(n - 2, memo)
        return memo[n]

    return dfs(n, memo)


def count_paths(n: int) -> int:
    memo = {}

    def dfs(n, memo):
        if n == 0:
            return 1

        if n <= 2:
            return n

        if n in memo:
            return memo[n]

        memo[n] = (
            dfs(n - 1, memo)
            + dfs(n - 2, memo)
            + dfs(n - 3, memo)
        )
        return memo[n]

    return dfs(n, memo)

# do not modify below this line
print(fibonacci(5))
print(fibonacci(8))

print(climb_stairs(3))
print(climb_stairs(4))

print(count_paths(3))
print(count_paths(5))

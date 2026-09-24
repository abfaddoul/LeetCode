class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        res = [0] * n

        for i in range(n - 2, -1, -1):
            j = i + 1

            while j < n and temperatures[j] <= temperatures[i]:
                if res[j] == 0:
                    break

                j += res[j]

            if j < n and temperatures[j] > temperatures[i]:
                res[i] = j - i

        return res
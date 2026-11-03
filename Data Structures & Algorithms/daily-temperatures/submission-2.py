class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][0]:
                stackt, stacki = stack.pop()
                res[stacki] = i - stacki
            stack.append((t,i))
        return res
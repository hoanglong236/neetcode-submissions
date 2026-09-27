class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []
        for i in range(n - 1, -1, -1):
            warmer_idx = i
            while stack:
                next_temperature, next_idx = stack[-1]
                if temperatures[i] < next_temperature:
                    warmer_idx = next_idx
                    break
                stack.pop()
            stack.append((temperatures[i], i))
            res[i] = warmer_idx - i
        return res
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        for i in range(n - 2, -1, -1):
            if temperatures[i] < temperatures[i + 1]:
                res[i] = 1
            else:
                count = 1
                while temperatures[i] >= temperatures[i + count]:
                    if res[i + count] == 0:
                        count = 0
                        break
                    count += res[i + count]
                res[i] = count
        return res
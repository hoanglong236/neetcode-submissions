class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        dest_times = [(target - position[i], (target - position[i]) / speed[i]) for i in range(n)]
        dest_times.sort(key=lambda x: x[0])
        res = 1
        stack = [dest_times[0][1]]
        for i in range(1, n):
            if dest_times[i][1] > stack[-1]:
                res += 1
                stack.append(dest_times[i][1])
        return res
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        nearest_indices = sorted(range(n), key=lambda x: target - position[x])
        res = 0
        last_arrived_time = -1
        for i in nearest_indices:
            time = (target - position[i]) / speed[i]
            if time > last_arrived_time:
                res += 1
                last_arrived_time = time
        return res
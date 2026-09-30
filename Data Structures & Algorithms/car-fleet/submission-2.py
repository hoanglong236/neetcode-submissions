class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        buckets = [0] * (target + 1)
        for i, pos in enumerate(position):
            buckets[target - pos] = (target - pos) / speed[i]

        res, last_time = 0, 0
        for time in buckets:
            if time != 0 and time > last_time:
                last_time = time
                res += 1
        return res
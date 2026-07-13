class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [(i, target - p) for i, p in enumerate(position)]
        distance.sort(key=lambda x: x[1])

        ans = 0
        top = -1
        for i, d in distance:
            t = d / speed[i]
            if t > top:
                top = t
                ans += 1
        return ans
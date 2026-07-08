from math import ceil

class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        closest = sorted(((i, target - p) for i, p in enumerate(position)), key=lambda x: x[1])
        stack = []
        for i, d in closest:
            v = d / speed[i]
            if not stack:
                stack.append(v)
            elif stack[-1] < v:
                stack.append(v)
        return len(stack)
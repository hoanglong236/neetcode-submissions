class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        distance = [(i, target - p) for i, p in enumerate(position)]
        distance.sort(key=lambda x: x[1])

        stack = []
        for i, d in distance:
            t = d / speed[i]
            if not stack:
                stack.append(t)
            elif t > stack[-1]:
                stack.append(t)
        return len(stack)
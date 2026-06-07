class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = [0] * n

        for i, h in enumerate(height):
            area[i] = max(min(max([0, *height[:i]]), max([0, *height[i+1:]])) - h, 0)

        return sum(area)
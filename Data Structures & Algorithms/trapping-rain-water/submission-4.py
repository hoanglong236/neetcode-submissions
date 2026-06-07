class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_r_prefix = [0] * n

        max_r = 0
        for i in range(n - 1, -1, -1):
            max_r = max(max_r, height[i])
            max_r_prefix[i] = max_r

        area = 0
        max_l = 0
        for i, h in enumerate(height):
            max_l = max(max_l, h)
            area += min(max_l, max_r_prefix[i]) - h
        return area
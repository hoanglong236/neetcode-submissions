class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        area = [0] * n
        max_l_prefix = [0] * n
        max_r_prefix = [0] * n

        max_l, max_r = 0, 0
        for i in range(n):
            max_l = max(max_l, height[i])
            max_l_prefix[i] = max_l

            max_r = max(max_r, height[n - 1 - i])
            max_r_prefix[n - 1 - i] = max_r

        for i, h in enumerate(height):
            area[i] = max(min(max_l_prefix[i], max_r_prefix[i]) - h, 0)

        return sum(area)
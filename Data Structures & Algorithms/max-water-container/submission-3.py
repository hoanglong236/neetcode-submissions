class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        peaks = [(0, heights[0])]
        for i in range(1, len(heights)):
            for j, h in peaks:
                area = min(heights[i], h) * (i - j)
                ans = max(ans, area)
            if heights[i] > peaks[-1][1]:
                peaks.append((i, heights[i]))

        return ans
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        peaks = [(0, heights[0])]
        for i in range(1, len(heights)):
            if heights[i] > peaks[-1][1]:
                peaks.append((i, heights[i]))

        for i in range(1, len(heights)):
            for j, h in peaks:
                if j >= i:
                    break
                area = min(heights[i], h) * (i - j)
                ans = max(ans, area)
        return ans
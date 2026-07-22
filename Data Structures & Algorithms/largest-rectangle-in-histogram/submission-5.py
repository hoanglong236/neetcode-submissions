class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans, n = 0, len(heights)
        stack = []
        for i in range(n):
            top_idx = i
            while stack and stack[-1][1] > heights[i]:
                top_idx, top_h = stack.pop()
                ans = max(ans, top_h * (i - top_idx))
            stack.append((top_idx, heights[i]))

        while stack:
            i, h = stack.pop()
            ans = max(ans, h * (n - i))
        return ans
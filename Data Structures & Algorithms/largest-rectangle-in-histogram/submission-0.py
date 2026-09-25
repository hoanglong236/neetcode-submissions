class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res, n = 0, len(heights)
        stack = []
        for i, h in enumerate(heights):
            top_idx = i
            while stack and stack[-1][0] > h:
                top, top_idx = stack.pop()
                res = max(res, top * (i - top_idx))
            if not stack or stack[-1][0] < h:
                stack.append([h, top_idx])
        while stack:
            top, top_idx = stack.pop()
            res = max(res, top * (n - top_idx))
        return res
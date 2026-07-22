class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = heights[0]
        stack = []
        for i in range(len(heights)):
            while len(stack) > heights[i]:
                stack.pop()
            for j in range(heights[i]):
                if j < len(stack):
                    stack[j] += j + 1
                    res = max(res, stack[j])
                else:
                    stack.append(j + 1)
                    res = max(res, stack[-1])
        return res
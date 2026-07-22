class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        for i in range(len(heights)):
            if not stack:
                stack.append((i, heights[i]))
            else:
                area = 0
                ci = i
                while stack and stack[-1][1] > heights[i]:
                    pi, ph = stack.pop()
                    area = max(area, ph * (i - pi))
                    ci = pi
                stack.append((ci, heights[i]))
                ans = max(ans, area)
            # print(stack)

        # print(stack, ans)
        while stack:
            i, h = stack.pop()
            ans = max(ans, h * (len(heights) - i))
        return ans
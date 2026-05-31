class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        for i in range(1, len(heights)):
            for j in range(0, i):
                width = min(heights[i], heights[j])
                height = i - j
                area = width * height
                ans = max(ans, area)
        return ans
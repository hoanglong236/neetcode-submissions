class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        left, right = 0, len(heights) - 1
        highest_left, highest_right = heights[left], heights[right]
        while left < right:
            if heights[left] < heights[right]:
                res = max(res, (right - left) * heights[left])
                highest_left = max(highest_left, heights[left])
                left += 1
                while left < right and heights[left] < highest_left:
                    left += 1
            else:
                res = max(res, (right - left) * heights[right])
                highest_right = max(highest_right, heights[right])
                right -= 1
                while left < right and heights[right] < highest_right:
                    right -= 1
        return res
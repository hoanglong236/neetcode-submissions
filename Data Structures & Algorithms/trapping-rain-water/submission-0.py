class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height) - 1
        left_candidate, right_candidate = 0, 0
        while left < right:
            if height[left] <= height[right]:
                left_candidate = max(left_candidate, height[left])
                res += left_candidate - height[left]
                left += 1
            else:
                right_candidate = max(right_candidate, height[right])
                res += right_candidate - height[right]
                right -= 1
        return res
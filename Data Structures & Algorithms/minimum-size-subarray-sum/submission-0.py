class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans, start, total = len(nums) + 1, 0, 0
        for end in range(len(nums)):
            total += nums[end]
            while total >= target:
                ans = min(ans, end - start + 1)
                total -= nums[start]
                start += 1
        if ans == len(nums) + 1:
            return 0
        return ans
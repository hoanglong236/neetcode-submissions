class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) + 1
        start, total = 0, 0
        for end in range(len(nums)):
            total += nums[end]
            if end - start + 1 > ans:
                total -= nums[start]
                start += 1
            if total >= target:
                while total - nums[start] >= target:
                    total -= nums[start]
                    start += 1
                ans = end - start + 1
        return 0 if ans > len(nums) else ans
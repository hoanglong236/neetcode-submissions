class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        res = n + 1
        running, start = 0, 0
        for i in range(n):
            running += nums[i]
            while running >= target:
                res = min(res, i - start + 1)
                running -= nums[start]
                start += 1
        return res if res <= n else 0
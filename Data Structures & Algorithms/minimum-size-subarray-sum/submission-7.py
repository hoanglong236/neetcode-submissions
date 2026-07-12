class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        running = [0] * (n + 1)
        for i, v in enumerate(nums):
            running[i + 1] = running[i] + v

        left, right = 1, n + 1
        while left < right:
            mid = (left + right) >> 1
            found = False
            for i in range(n - mid + 1):
                if running[i + mid] - running[i] >= target:
                    found = True
                    break
            if found:
                right = mid
            else:
                left = mid + 1
        return right if right <= n else 0
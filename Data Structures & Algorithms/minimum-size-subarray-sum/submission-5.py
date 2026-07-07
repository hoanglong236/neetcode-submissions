class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefix = [0] * (len(nums) + 1)
        total = 0
        for idx, num in enumerate(nums):
            total += num
            prefix[idx + 1] = total

        start, end = 1, len(nums)
        while start < end:
            mid = (start + end) >> 1
            move_left = False
            for i in range(mid, len(nums) + 1):
                if prefix[i] - prefix[i - mid] >= target:
                    move_left = True
                    break
            if move_left:
                end = mid
            else:
                start = mid + 1
        return 0 if start == len(nums) and prefix[-1] < target else start

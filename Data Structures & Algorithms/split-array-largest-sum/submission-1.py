class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        left, right = 0, sum(nums)

        while left < right:
            mid = (left + right) // 2
            i = 0
            for _ in range(k):
                sub_sum = 0
                while i < n and sub_sum + nums[i] <= mid:
                    sub_sum += nums[i]
                    i += 1
                if i == n:
                    right = mid
                    break
            if i < n:
                left = mid + 1
        return left
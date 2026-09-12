class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        while left < right:
            mid = (left + right) >> 1
            target = mid
            tmp = k
            cur = 0
            for i in range(len(nums)):
                if cur + nums[i] <= target:
                    cur += nums[i]
                else:
                    tmp -= 1
                    cur = nums[i]
                if tmp < 0:
                    break
            if cur != 0:
                tmp -= 1
            if tmp < 0:
                left = mid + 1
            else:
                right = mid
        return left
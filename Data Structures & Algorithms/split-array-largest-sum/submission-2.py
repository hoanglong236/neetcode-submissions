class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def splitable(target):
            segments, curr_sum = 1, 0
            for num in nums:
                if curr_sum + num > target:
                    segments += 1
                    curr_sum = num
                    if segments > k:
                        return False
                else:
                    curr_sum += num
            return segments <= k

        while left < right:
            mid = (left + right) >> 1
            if not splitable(mid):
                left = mid + 1
            else:
                right = mid
        return left
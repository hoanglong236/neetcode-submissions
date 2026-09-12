class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def splitable(nums, target, group):
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > target:
                    group -= 1
                    curr_sum = num
                    if group < 0:
                        return False
            group -= int(curr_sum > 0)
            return group >= 0

        while left < right:
            mid = (left + right) >> 1
            if not splitable(nums, mid, k):
                left = mid + 1
            else:
                right = mid
        return left
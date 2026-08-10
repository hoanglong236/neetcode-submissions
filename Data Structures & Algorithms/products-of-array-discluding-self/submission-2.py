class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        tmp = 1
        for i in range(1, n):
            tmp *= nums[i - 1]
            res[i] = tmp

        tmp = 1
        for i in range(1, n):
            tmp *= nums[n - i]
            res[n - 1 - i] *= tmp

        return res
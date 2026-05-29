class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, n = 0, len(nums)
        while i < n:
            if nums[i] > n or nums[i] <= 0 or nums[i] == i + 1:
                i += 1
            elif nums[i] == nums[nums[i] - 1]:
                i += 1
            else:
                tmp = nums[i]
                nums[i], nums[tmp - 1] = nums[tmp - 1], tmp

        for i, num in enumerate(nums):
            if num != i + 1:
                return i + 1
        return len(nums) + 1

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start, end = 0, len(nums) - 1
        i = 0
        while i < len(nums):
            if nums[i] == 0 and start < i:
                nums[start], nums[i] = nums[i], nums[start]
                start += 1
            elif nums[i] == 2 and i < end:
                nums[end], nums[i] = nums[i], nums[end]
                end -= 1
            else:
                i += 1
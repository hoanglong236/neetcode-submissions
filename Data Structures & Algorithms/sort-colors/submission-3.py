class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return

        left, right = -1, len(nums)
        cur = left + 1
        while cur < right:
            if nums[cur] == 0:
                left += 1
                nums[left], nums[cur] = nums[cur], nums[left]
                if left == cur:
                    cur += 1
            elif nums[cur] == 2:
                right -= 1
                nums[right], nums[cur] = nums[cur], nums[right]
            else:
                cur += 1
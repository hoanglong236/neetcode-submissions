class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0

        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] != val:
                left += 1
            if nums[right] == val:
                right -= 1
            if nums[left] == val and nums[right] != val:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if left == 0:
            return 0
        return left if nums[left] == val else left + 1
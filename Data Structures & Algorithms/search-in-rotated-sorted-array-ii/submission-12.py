class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] == nums[right]:
                return (
                    self.search(nums[left:max(left, mid - 1) + 1], target)
                    or self.search(nums[mid + 1:max(mid + 1, right) + 1], target)
                )
            if nums[mid] < target and target <= nums[right]:
                left = mid + 1
            elif nums[mid] < target and nums[left] < nums[mid]:
                left = mid + 1
            elif nums[mid] < target and nums[left] == nums[mid] and nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] > target and nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums and nums[left] == target
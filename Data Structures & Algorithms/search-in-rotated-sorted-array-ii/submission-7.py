class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[right] == target:
                return True

            if nums[mid] > target:
                if target < nums[right]:
                    if nums[mid] < nums[right]:
                        right = mid - 1
                    elif nums[mid] > nums[right]:
                        left = mid + 1
                    else:
                        right -= 1
                else:
                    right = mid - 1

            else:
                if target < nums[right]:
                    right = mid - 1
                else:
                    if nums[mid] < nums[right]:
                        right = mid - 1
                    elif nums[mid] > nums[right]:
                        left = mid + 1
                    else:
                        right -= 1
        return False
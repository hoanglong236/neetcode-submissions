class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_left = nums[mid] > nums[right]
            target_left = target > nums[right]
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if target_left:
                    right = mid - 1
                elif mid_left:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target_left:
                    if not mid_left:
                        right = mid - 1
                    else:
                        left = mid + 1
                else:
                    left = mid + 1
        return -1
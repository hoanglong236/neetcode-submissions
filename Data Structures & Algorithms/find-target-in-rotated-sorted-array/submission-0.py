class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        target_left_branch = target > nums[right]
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                if target_left_branch:
                    right = mid - 1
                else:
                    if nums[mid] > nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
            else:
                if target_left_branch:
                    if nums[mid] > nums[-1]:
                        left = mid + 1
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
        return -1
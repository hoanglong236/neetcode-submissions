class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        no_rotate = nums[0] < nums[-1]
        target_left_branch = no_rotate or target > nums[-1]
        while left < right:
            mid = (left + right) // 2
            mid_left_branch = no_rotate or nums[mid] > nums[-1]
            if nums[mid] < target:
                if target_left_branch:
                    if mid_left_branch:
                        left = mid + 1
                    else:
                        right = mid
                else:
                    left = mid + 1
            else:
                if target_left_branch:
                    right = mid
                else:
                    if mid_left_branch:
                        left = mid + 1
                    else:
                        right = mid
        return left if nums[left] == target else -1
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        target_left_branch = False
        if target == nums[right]:
            return True
        elif target > nums[right]:
            target_left_branch = True
        print(target_left_branch)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                if nums[mid] == nums[right]:
                    right -= 1
                elif nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    if target_left_branch:
                        if nums[left] < nums[right]:
                            left = mid + 1
                        else:
                            right = mid
                    else:
                        left = mid + 1
            else:
                if nums[mid] == nums[right]:
                    right -= 1
                elif nums[mid] > nums[right]:
                    if target_left_branch:
                        right = mid
                    else:
                        left = mid + 1
                else:
                    right = mid
        return nums[left] == target
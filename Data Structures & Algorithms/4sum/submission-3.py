class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if target >= 0 and nums[i] > target:
                break
            for j in range(i + 1, len(nums) - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if left > j + 1 and nums[left] == nums[left - 1]:
                        left += 1
                        continue
                    if right + 1 < len(nums) and nums[right] == nums[right + 1]:
                        right -= 1
                        continue
                    val = nums[i] + nums[j] + nums[left] + nums[right]
                    if val < target:
                        left += 1
                    elif val > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
        return res
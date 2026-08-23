class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        idx, n = 0, len(nums)
        while idx < n:
            val = nums[idx]
            if val <= 0:
                idx += 1
            else:
                if val != idx + 1 and val < n and nums[val - 1] != val:
                    nums[idx], nums[val - 1] = nums[val - 1], val
                else:
                    idx += 1
        idx = 0
        while idx < n:
            if nums[idx] != idx + 1:
                break
            idx += 1
        return idx + 1
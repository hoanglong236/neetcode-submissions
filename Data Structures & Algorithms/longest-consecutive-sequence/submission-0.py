class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        nums.sort()
        ans = 0
        cur_size = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur_size += 1
            elif nums[i] != nums[i - 1]:
                ans = max(cur_size, ans)
                cur_size = 1
        return max(cur_size, ans)
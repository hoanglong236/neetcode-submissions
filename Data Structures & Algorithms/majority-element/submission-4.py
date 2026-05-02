class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, step = nums[0], 0
        for num in nums:
            if step == 0:
                ans = num
                step = 1
            else:
                step += 1 if num == ans else -1
        return ans
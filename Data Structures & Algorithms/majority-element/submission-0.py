class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        el, count = nums[0], 0
        for num in nums:
            if count == 0:
                el, count = num, 1
            else:
                count += 1 if el == num else - 1
        return el
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        freq = {}
        for i in range(len(nums)):
            j = freq.get(target - nums[i], -1)
            if j > -1:
                return [j, i]
            freq[nums[i]] = i
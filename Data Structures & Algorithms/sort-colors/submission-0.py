class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        buckets = [0] * 3
        for num in nums:
            buckets[num] += 1
        i = 0
        for num, count in enumerate(buckets):
            for _ in range(count):
                nums[i] = num
                i += 1
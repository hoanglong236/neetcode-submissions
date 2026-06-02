class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 1

        p1, p2 = 0, 1
        while p2 < len(nums):
            if nums[p1] < nums[p2]:
                if p1 + 1 < p2:
                    nums[p1 + 1] = nums[p2]
                p1 += 1
            p2 += 1
        return p1 + 1
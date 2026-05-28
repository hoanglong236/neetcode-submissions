class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = set()
        nums.sort()

        for i in range(0, len(nums) - 3):
            for j in range(i + 1, len(nums) - 2):
                for k in range(j + 1, len(nums) - 1):
                    for h in range(k + 1, len(nums)):
                        if nums[i] + nums[j] + nums[k] + nums[h] == target:
                            ans.add((nums[i], nums[j], nums[h], nums[k]))
        return [list(x) for x in ans]
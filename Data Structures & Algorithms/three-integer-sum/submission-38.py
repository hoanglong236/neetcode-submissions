class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i, x in enumerate(nums):
            if x > 0:
                break
            if i > 0 and x == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                three_sum = x + nums[l] + nums[r]
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    ans.append([x, nums[l], nums[r]])
                    while (
                        l < r
                        and nums[l] == nums[l + 1] and nums[r] == nums[r - 1]
                    ):
                        l += 1
                        r -= 1
                    l += 1
                    r -= 1

        return ans
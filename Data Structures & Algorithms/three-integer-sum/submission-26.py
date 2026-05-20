from collections import defaultdict

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()

        freq = defaultdict(list)
        for i, num in enumerate(nums):
            freq[num].append(i)

        left, right = 0, len(nums) - 1

        while left < right:
            for i in range(left + 1, right + 1):
                target = 0 - nums[left] - nums[i]    
                for j in freq[target]:
                    if left < j and j < i:
                        tmp = [nums[left], nums[j], nums[i]]
                        ans.add(tuple(tmp))
                        break
            left += 1

        return [list(x) for x in ans]
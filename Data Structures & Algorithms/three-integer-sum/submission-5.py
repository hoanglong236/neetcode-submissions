class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        triples = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                if left > i + 1 and nums[left] == nums[left - 1]:
                    left += 1
                    continue
                if right < len(nums) - 1 and nums[right] == nums[right + 1]:
                    right -= 1
                    continue
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    triples.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return triples
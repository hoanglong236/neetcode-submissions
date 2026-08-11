class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, v in enumerate(nums):
            seen_idx = seen.get(target - v, -1)
            if seen_idx > -1:
                return [seen_idx, i]
            seen[v] = i
        return [-1, -1]
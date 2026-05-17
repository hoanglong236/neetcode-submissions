class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        positive = set(filter(lambda x: x > 0, nums))
        if len(positive) == 0:
            return 1
        
        ans = 1
        while ans in positive:
            ans += 1
        return ans
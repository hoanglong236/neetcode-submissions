class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        ans = 0
        for num in seen:
            if num - 1 not in seen:
                cur_size = 1
                while num + 1 in seen:
                    num += 1
                    cur_size += 1
                ans = max(ans, cur_size)
        return ans
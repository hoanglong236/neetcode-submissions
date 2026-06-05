class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                count, current = 0, num
                while current in num_set:
                    count += 1
                    current += 1
                ans = max(ans, count)
        return ans


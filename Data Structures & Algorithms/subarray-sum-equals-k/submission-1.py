from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, running_sum = 0, 0
        freq_sum = defaultdict(int)
        freq_sum[0] = 1
        for num in nums:
            running_sum += num
            res += freq_sum[running_sum - k]
            freq_sum[running_sum] += 1
        return res
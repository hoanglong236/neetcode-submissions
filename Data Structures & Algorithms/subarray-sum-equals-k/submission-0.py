class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res, running_sum = 0, 0
        freq_sum = {0: 1}
        for num in nums:
            running_sum += num
            if running_sum - k in freq_sum:
                res += freq_sum[running_sum - k]
            freq_sum[running_sum] = freq_sum.get(running_sum, 0) + 1
        return res
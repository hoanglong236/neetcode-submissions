class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        # Initialize with {0: 1} to account for subarrays starting at index 0.
        prefix_sum = {0: 1}
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum - k in prefix_sum:
                ans += prefix_sum[current_sum - k]
            prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1
        return ans
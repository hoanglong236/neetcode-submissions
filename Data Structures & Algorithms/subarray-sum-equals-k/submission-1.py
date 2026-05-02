from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        current_sum = 0

        prefix_sum = defaultdict(int)
        # Must have to count these cases:
        # Subarrays start with index 0
        # The element itself equals k
        prefix_sum[0] = 1

        for num in nums:
            current_sum += num
            ans += prefix_sum[current_sum - k]
            prefix_sum[current_sum] += 1
        return ans
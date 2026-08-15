from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = defaultdict(list)
        most = 0
        for num, count in freq.items():
            buckets[count].append(num)
            most = max(most, count)

        ans = []
        for i in range(most, 0, -1):
            ans.extend(buckets[i])
            if len(ans) >= k:
                break
        return ans[:k]
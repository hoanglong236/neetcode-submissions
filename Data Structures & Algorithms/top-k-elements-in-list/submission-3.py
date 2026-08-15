class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [0] * 2001
        minimum = 1000
        most = 0
        for num in nums:
            freq[num + minimum] += 1
            most = max(most, freq[num + minimum])

        buckets = [[] for _ in range(most + 1)]
        for num, count in enumerate(freq):
            if count > 0:
                buckets[count].append(num - minimum)

        ans = []
        for i in range(most, 0, -1):
            ans.extend(buckets[i])
            if len(ans) >= k:
                break
        return ans[:k]
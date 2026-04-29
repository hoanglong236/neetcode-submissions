class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [0] * 2001
        for num in nums:
            freq[num + 1000] += 1

        buckets = [[] for i in range(max(freq) + 1)]
        for i, v in enumerate(freq):
            buckets[v].append(i - 1000)
        
        ans = []
        i = len(buckets) - 1
        for _ in range(k):
            while len(buckets[i]) == 0:
                i -= 1

            ans.append(buckets[i].pop())
        return ans
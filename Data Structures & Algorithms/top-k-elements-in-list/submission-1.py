class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        buckets = {}
        for num, count in freq.items():
            arr = buckets.get(count, [])
            arr.append(num)
            buckets[count] = arr

        ans = []
        sorted_buckets = sorted(buckets.items(), key=lambda x: x[0], reverse=True)
        r, c = 0, 0
        for _ in range(k):
            if c == len(sorted_buckets[r][1]):
                c = 0
                r += 1
            ans.append(sorted_buckets[r][1][c])
            c += 1
        return ans
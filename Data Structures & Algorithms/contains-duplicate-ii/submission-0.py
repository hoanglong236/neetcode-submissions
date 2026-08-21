class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq = {}
        for i, v in enumerate(nums):
            last = freq.get(v, -1)
            if last > -1 and i - last <= k:
                return True
            freq[v] = i
        return False
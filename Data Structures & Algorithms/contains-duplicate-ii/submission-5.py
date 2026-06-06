class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        for i in range(len(nums)):
            start, end = i, min(i + k + 1, len(nums))
            unique = set(nums[start:end])
            if len(unique) < end - start:
                return True
        return False
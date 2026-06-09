class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        distinct = set()
        for i, num in enumerate(nums):
            if i > k:
                distinct.remove(nums[i - k - 1])
            if num in distinct:
                return True
            distinct.add(num)
        return False
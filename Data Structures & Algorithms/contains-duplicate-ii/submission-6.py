class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p1, p2 = 0, min(k, len(nums) - 1)
        distinct = set(nums[p1:p2 + 1])
        if len(distinct) < p2 - p1 + 1:
            return True
        
        for i in range(p2 + 1, len(nums)):
            distinct.remove(nums[p1])
            if nums[i] in distinct:
                return True
            distinct.add(nums[i])
            p1 += 1
        return False
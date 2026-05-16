class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) < 3:
            return list(set(nums))
        
        p1, p1_count = nums[0], 0
        p2, p2_count = nums[0], 0

        for num in nums:
            if num == p1 and p1_count > 0:
                p1_count += 1
            elif num == p2 and p2_count > 0:
                p2_count += 1
            elif p1_count == 0:
                p1, p1_count = num, 1
            elif p2_count == 0:
                p2, p2_count = num, 1
            else:
                p1_count -= 1
                p2_count -= 1
        
        p1_count, p2_count = 0, 0
        for num in nums:
            if num == p1:
                p1_count += 1
            elif num == p2:
                p2_count += 1
        
        ans = []
        if p1_count > len(nums) / 3:
            ans.append(p1)
        if p2_count > len(nums) / 3:
            ans.append(p2)
        return ans
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) <= 2:
            return nums

        p1, p1_count = None, 0
        p2, p2_count = None, 0

        for num in nums:
            if num == p1:
                p1_count += 1
            elif num == p2:
                p2_count += 1
            else:
                if p1_count == 0:
                    p1, p1_count = num, 1
                elif p2_count == 0:
                    p2, p2_count = num, 1
                else:
                    p1_count -= 1
                    p2_count -= 1

        p1_count = 0
        p2_count = 0
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

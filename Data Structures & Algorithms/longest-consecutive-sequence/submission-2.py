class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        ans = 0
        tracking = {num: False for num in nums}
        for num in nums:
            if not tracking[num]:
                start, end = num, num
                while start - 1 in tracking:
                    start -= 1
                    tracking[start] = True
                while end + 1 in tracking:
                    end += 1
                    tracking[end] = True
                ans = max(ans, end - start + 1)
        return ans
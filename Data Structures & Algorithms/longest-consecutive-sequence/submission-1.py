class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        ans = 0
        nums_dict = {num: 0 for num in nums}
        for num in nums:
            if nums_dict[num] == 0:
                start = num
                end = num
                while start - 1 in nums_dict:
                    start -= 1
                    nums_dict[start] = 1
                while end + 1 in nums_dict:
                    end += 1
                    nums_dict[end] = 1
            ans = max(ans, end - start + 1)
        return ans
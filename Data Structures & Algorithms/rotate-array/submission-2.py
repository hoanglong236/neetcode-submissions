class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        ans = [nums[i - k] for i in range(n)]
        for i in range(n):
            nums[i] = ans[i]
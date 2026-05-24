class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return

        left_size, right_size = n - k, k
        left, right = 0, n - k
        while left_size != 0 and right_size != 0:
            for _ in range(min(left_size, right_size)):
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right += 1

            if left_size < right_size:
                right_size -= left_size
            else:
                left_size -= right_size
                right -= right_size
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
        left_start, right_start = 0, n - k
        while left_size != 0 and right_size != 0:
            for _ in range(min(left_size, right_size)):
                nums[left_start], nums[right_start] = nums[right_start], nums[left_start]
                left_start += 1
                right_start += 1

            if left_size < right_size:
                right_size -= left_size
            else:
                left_size -= right_size
                right_start -= right_size
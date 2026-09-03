class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        if k == 0:
            return
        count = 0
        remain = n - k
        cycle = k
        cycle_idx = n - cycle
        for i in range(n):
            nums[i], nums[cycle_idx] = nums[cycle_idx], nums[i]
            cycle_idx += 1
            count += 1
            if remain < cycle and count == remain:
                cycle = cycle - remain
                cycle_idx = n - cycle
                count = 0
            elif count == cycle:
                remain -= cycle
                count = 0
                cycle_idx = n - cycle
            # print(nums, remain, cycle, i, count)
                
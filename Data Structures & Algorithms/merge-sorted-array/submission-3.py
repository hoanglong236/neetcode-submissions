class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1, p2 = 0, 0
        nums = [0] * (m + n)
        for i in range(m + n):
            if p1 == m:
                nums[i] = nums2[p2]
                p2 += 1
            elif p2 == n:
                nums[i] = nums1[p1]
                p1 += 1
            elif nums1[p1] <= nums2[p2]:
                nums[i] = nums1[p1]
                p1 += 1
            else:
                nums[i] = nums2[p2]
                p2 += 1
        for i in range(m + n):
            nums1[i] = nums[i]
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m + i] = nums2[i]

        p1, p2 = 0, m
        while p1 < p2 and p2 < m + n:
            if nums1[p1] > nums1[p2]:
                nums1[p1], nums1[p2] = nums1[p2], nums1[p1]
                if p2 == m + n - 1:
                    p2 = m
                elif p2 < m + n - 1 and nums1[p2] > nums1[p2 + 1]:
                    p2 += 1
            p1 += 1
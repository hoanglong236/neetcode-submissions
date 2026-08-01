class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        d, mod = divmod(m + n, 2)
        prev, cur = 0, 0
        i, j = 0, 0
        for _ in range(d + 1):
            prev = cur
            if i == m:
                cur = nums2[j]
                j += 1
            elif j == n:
                cur = nums1[i]
                i += 1
            elif nums1[i] <= nums2[j]:
                cur = nums1[i]
                i += 1
            else:
                cur = nums2[j]
                j += 1
        if mod == 0:
            return (cur + prev) / 2
        return cur
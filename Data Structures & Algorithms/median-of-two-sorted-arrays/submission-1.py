class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = nums1, nums2
        if len(nums1) > len(nums2):
            arr1, arr2 = nums2, nums1
        n1, n2 = len(arr1), len(arr2)
        total = n1 + n2
        half = total // 2

        left, right = 0, n1 - 1
        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2

            v1 = arr1[mid1] if mid1 >= 0 else float('-inf')
            v1_next = arr1[mid1 + 1] if mid1 + 1 < n1 else float('inf')
            v2 = arr2[mid2] if mid2 >= 0 else float('-inf')
            v2_next = arr2[mid2 + 1] if mid2 + 1 < n2 else float('inf')

            if v2 <= v1_next and v1 <= v2_next:
                median1, median2 = max(v1, v2), min(v1_next, v2_next)
                if total % 2 != 0:
                    return max(median1, median2)
                else:
                    return (median1 + median2) / 2
            elif v1 > v2_next:
                right = mid1 - 1
            else:
                left = mid1 + 1
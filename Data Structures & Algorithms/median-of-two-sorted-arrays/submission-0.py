class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr = sorted(nums1 + nums2)
        d, m = divmod(len(arr), 2)
        if m == 0:
            return (arr[d] + arr[d - 1]) / 2
        return arr[d]
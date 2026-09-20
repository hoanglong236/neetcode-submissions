class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        d, m = divmod(n, 2)
        return nums[d] if m == 1 else (nums[d - 1] + nums[d]) / 2
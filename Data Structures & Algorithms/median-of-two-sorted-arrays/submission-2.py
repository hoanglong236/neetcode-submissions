class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        nums = [0] * (n1 + n2)
        i, j, k = 0, 0, 0
        while i < n1 and j < n2:
            if nums1[i] <= nums2[j]:
                nums[k] = nums1[i]
                i += 1
            else:
                nums[k] = nums2[j]
                j += 1
            k += 1
        while i < n1:
            nums[k] = nums1[i]
            k += 1
            i += 1
        while j < n2:
            nums[k] = nums2[j]
            k += 1
            j += 1
        d, m = divmod(n1 + n2, 2)
        return nums[d] if m == 1 else (nums[d - 1] + nums[d]) / 2
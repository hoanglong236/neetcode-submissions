class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)

        # 0, pivot -> Non-desc array
        # pivot, n - 1 -> Non-desc array
        def findPivotIdx():
            left, right = 0, n - 1
            while left < right:
                while left < right and nums[left] == nums[right]:
                    left += 1
                mid = (left + right) // 2
                if nums[mid] > nums[right]:
                    left = mid + 1
                elif nums[mid] <= nums[right]:
                    right = mid
            return left

        def binarySearchNonDESC(left, right):
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    return True
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        pivotIdx = findPivotIdx()
        if target > nums[n - 1]:
            return binarySearchNonDESC(0, pivotIdx - 1)
        return binarySearchNonDESC(pivotIdx, n - 1)
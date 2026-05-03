class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSortedArrays(arr1, arr2, result):
            i = j = k = 0
            while i < len(arr1) and j < len(arr2):
                if arr1[i] <= arr2[j]:
                    result[k] = arr1[i]
                    i += 1
                else:
                    result[k] = arr2[j]
                    j += 1
                k += 1
            while i < len(arr1):
                result[k] = arr1[i]
                k += 1
                i += 1
            while j < len(arr2):
                result[k] = arr2[j]
                k += 1
                j += 1

        def mergeSort(array):
            if len(array) < 2:
                return
            mid = len(array) // 2
            left = array[:mid]
            right = array[mid:]

            mergeSort(left)
            mergeSort(right)

            mergeSortedArrays(left, right, array)

        mergeSort(nums)
        return nums        
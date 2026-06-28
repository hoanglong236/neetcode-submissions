class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        l, r = 0, len(arr) - 1
        while l < r:
            middle = (l + r) // 2
            if abs(arr[middle] - x) <= abs(arr[middle + 1] - x):
                r = middle
            else:
                l = middle + 1

        l = max(l - k, 0)
        for r in range(l + k, len(arr)):
            if abs(arr[l] - x) <= abs(arr[r] - x):
                break
            l += 1
        return arr[l:l + k]
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        l, r = 0, len(arr) - 1
        nearest = l
        while l < r:
            middle = (l + r) // 2
            if abs(arr[middle] - x) <= abs(arr[middle + 1] - x):
                r = middle
                nearest = r
            else:
                l = middle + 1
                nearest = l

        l = max(nearest - k, 0)
        while l + k < len(arr) and abs(arr[l] - x) > abs(arr[l + k] - x):
            l += 1
        return arr[l:l + k]
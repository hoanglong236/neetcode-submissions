class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr

        l = 0
        for r in range(l + k, len(arr)):
            if abs(arr[l] - x) > abs(arr[r] - x):
                l += 1
            elif abs(arr[l] - x) < abs(arr[r] - x):
                break
        return arr[l:l + k]
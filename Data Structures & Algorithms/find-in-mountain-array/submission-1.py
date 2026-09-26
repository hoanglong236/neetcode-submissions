class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        heights = {}

        def cacheHeight(idx):
            if idx not in heights:
                h = mountainArr.get(idx)
                heights[idx] = h
                return h
            return heights[idx]

        def findMountainIndex():
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                height = cacheHeight(mid)
                next_height = cacheHeight(mid + 1)
                if height > next_height:
                    prev_height = cacheHeight(mid - 1)
                    if height > prev_height:
                        return mid
                    else:
                        right = mid - 1
                else:
                    left = mid + 1
            return left

        def binarySearchASC(left, right):
            while left <= right:
                mid = (left + right) // 2
                height = heights[mid] if mid in heights else mountainArr.get(mid)
                if height == target:
                    return mid
                if height < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        def binarySearchDESC(left, right):
            while left <= right:
                mid = (left + right) // 2
                height = heights[mid] if mid in heights else mountainArr.get(mid)
                if height == target:
                    return mid
                if height < target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1

        mountainIdx = findMountainIndex()
        res = binarySearchASC(0, mountainIdx)
        return res if res != -1 else binarySearchDESC(mountainIdx + 1, n - 1)
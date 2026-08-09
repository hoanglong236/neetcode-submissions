from math import ceil

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            count = h
            for pile in piles:
                count -= ceil(pile / mid)
                if count < 0:
                    break
            if count < 0:
                left = mid + 1
            else:
                right = mid
        return left
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)
        while left < right:
            mid = (left + right) // 2
            hour = 0
            for p in piles:
                hour += p // mid + int(p % mid != 0)
            if hour > h:
                left = mid + 1
            else:
                right = mid
        return left
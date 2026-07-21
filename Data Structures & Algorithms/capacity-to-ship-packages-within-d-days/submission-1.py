class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            capacity, count = mid, days - 1
            for w in weights:
                if capacity < w:
                    capacity = mid
                    count -= 1
                    if count < 0:
                        break
                capacity -= w
            if count < 0:
                left = mid + 1
            else:
                right = mid
        return left
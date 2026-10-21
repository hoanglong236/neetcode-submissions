class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) >> 1
            cap, ship_days = mid, 1
            for w in weights:
                if cap < w:
                    cap = mid
                    ship_days += 1
                cap -= w
                if ship_days > days:
                    break
            if ship_days <= days:
                right = mid
            else:
                left = mid + 1
        return left
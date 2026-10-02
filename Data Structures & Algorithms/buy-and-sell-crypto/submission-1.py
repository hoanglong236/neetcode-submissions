class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_day = 0
        for day in range(len(prices)):
            if prices[day] > prices[buy_day]:
                profit = max(profit, prices[day] - prices[buy_day])
            else:
                buy_day = day
        return profit
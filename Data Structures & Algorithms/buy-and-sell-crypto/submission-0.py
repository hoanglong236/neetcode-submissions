class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_day, sell_day = 0, 0
        profit = 0
        for i in range(len(prices)):
            if prices[i] < prices[buy_day]:
                profit = max(profit, prices[sell_day] - prices[buy_day])
                buy_day = i
                sell_day = i + 1
            elif prices[i] > prices[sell_day]:
                sell_day = i
        if sell_day < len(prices):
            return max(profit, prices[sell_day] - prices[buy_day])
        return profit
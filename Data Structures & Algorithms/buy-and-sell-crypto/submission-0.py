class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = prices[0]
        for price in prices:
            if price > buy:
                profit = max(profit, price - buy)
            else:
                buy = price
        return profit
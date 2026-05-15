class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy, sell = prices[0], -1
        i = 1
        while i < len(prices):
            if prices[i] > buy:
                if prices[i] > sell:
                    sell = prices[i]
                else:
                    profit += sell - buy
                    buy = prices[i]
                    sell = -1
            else:
                if sell > -1:
                    profit += sell - buy
                    sell = -1
                buy = prices[i]
            i += 1
        if sell > -1:
            profit += sell - buy
        return profit


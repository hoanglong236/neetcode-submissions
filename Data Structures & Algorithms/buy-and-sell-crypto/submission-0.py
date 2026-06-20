class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans, buy = 0, 0
        for sell in range(len(prices)):
            if prices[buy] > prices[sell]:
                buy = sell
            if prices[sell] - prices[buy] > ans:
                ans = prices[sell] - prices[buy]
        return ans
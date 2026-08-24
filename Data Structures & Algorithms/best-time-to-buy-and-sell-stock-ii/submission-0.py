class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy = prices[0]
        for price in prices:
            if price > buy:
                ans += price - buy
            buy = price
        return ans
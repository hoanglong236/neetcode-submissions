class StockSpanner:

    def __init__(self):
        self.prices = []

    def next(self, price: int) -> int:
        freq = 1
        while self.prices:
            prev_price, prev_freq = self.prices[-1]
            if prev_price > price:
                break
            else:
                self.prices.pop()
                freq += prev_freq

        self.prices.append((price, freq))
        return freq


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
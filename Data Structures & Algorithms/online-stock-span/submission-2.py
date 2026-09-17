class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        rev_stack = []
        while self.stack and self.stack[-1] <= price:
            rev_stack.append(self.stack.pop())
            span += 1
        while rev_stack:
            self.stack.append(rev_stack.pop())
        self.stack.append(price)
        return span



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
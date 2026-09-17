class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        if not self.stack:
            self.stack.append([price, 1])
        else:
            rev_stack = []
            top = [price, 1]
            while self.stack:
                rev_stack.append(self.stack.pop())
                if rev_stack[-1][0] > price:
                    break
                top[1] += 1
            while rev_stack:
                self.stack.append(rev_stack.pop())
            self.stack.append(top)
        return self.stack[-1][1]



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
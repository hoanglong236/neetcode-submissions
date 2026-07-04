class FreqStack:

    def __init__(self):
        self.freq = dict()
        self.most = 0
        self.freq_stack = []

    def push(self, val: int) -> None:
        self.freq[val] = self.freq.get(val, 0) + 1
        if self.freq[val] > self.most:
            self.most = self.freq[val]
            self.freq_stack.append([val])
        else:
            self.freq_stack[self.freq[val] - 1].append(val)

    def pop(self) -> int:
        val = self.freq_stack[self.most - 1].pop()
        self.freq[val] -= 1
        if not self.freq_stack[self.most - 1]:
            self.freq_stack.pop()
            self.most -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.freq_rev = {}
        self.max_freq = 0

    def push(self, val: int) -> None:
        curr_freq = self.freq.get(val, 0) + 1
        if self.max_freq < curr_freq:
            self.max_freq = curr_freq
        self.freq[val] = curr_freq
        elements = self.freq_rev.get(curr_freq, [])
        elements.append(val)
        self.freq_rev[curr_freq] = elements

    def pop(self) -> int:
        elements = self.freq_rev[self.max_freq]
        top = elements.pop()
        if not elements:
            self.max_freq -= 1
        self.freq[top] -= 1
        return top
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
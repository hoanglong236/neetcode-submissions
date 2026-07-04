class FreqStack:

    def __init__(self):
        self.freq = dict()
        self.size = 0

    def push(self, val: int) -> None:
        count, indices = self.freq.get(val, (0, [-1]))
        indices.append(self.size)

        self.freq[val] = (count + 1, indices)
        self.size += 1

    def pop(self) -> int:
        most = max(self.freq, key=lambda x: (self.freq[x][0], self.freq[x][1][-1]))
        count, indices = self.freq[most]
        indices.pop()
        self.freq[most] = (count - 1, indices)
        return most


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
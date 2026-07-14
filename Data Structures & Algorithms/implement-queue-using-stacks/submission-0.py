class MyQueue:

    def __init__(self):
        self.main = []
        self.backup = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while len(self.main) > 1:
            self.backup.append(self.main.pop())
        res = self.main.pop()
        while self.backup:
            self.main.append(self.backup.pop())
        return res

    def peek(self) -> int:
        while len(self.main) > 1:
            self.backup.append(self.main.pop())
        res = self.main[-1]
        while self.backup:
            self.main.append(self.backup.pop())
        return res

    def empty(self) -> bool:
        return not self.main


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
from collections import deque

class MyStack:

    def __init__(self):
        self.main = deque()
        self.topEl = deque()

    def push(self, x: int) -> None:
        while self.topEl:
            self.main.append(self.topEl.popleft())
        self.topEl.append(x)

    def pop(self) -> int:
        res = self.topEl.popleft()
        while len(self.main) > 1:
            self.topEl.append(self.main.popleft())
        self.main, self.topEl = self.topEl, self.main 
        return res

    def top(self) -> int:
        return self.topEl[0]

    def empty(self) -> bool:
        return not self.main and not self.topEl


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
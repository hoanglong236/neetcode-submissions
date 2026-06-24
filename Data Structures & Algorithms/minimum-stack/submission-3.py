class MinStack:

    def __init__(self):
        self.stack = []
        self.min_prefix_stack = []
        self.min_val = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(self.min_val, val)
        self.min_prefix_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_prefix_stack.pop()
        if self.min_prefix_stack:
            self.min_val = self.min_prefix_stack[-1]
        else:
            self.min_val = float('inf')

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_prefix_stack[-1]
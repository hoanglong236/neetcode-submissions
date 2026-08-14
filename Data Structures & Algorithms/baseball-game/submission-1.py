class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                d = stack.pop()
                total = d + stack[-1]
                stack.append(d)
                stack.append(total)
                res += stack[-1]
            elif op == 'D':
                stack.append(stack[-1] * 2)
                res += stack[-1]
            elif op == 'C':
                res -= stack.pop()
            else:
                stack.append(int(op))
                res += stack[-1]
        return res
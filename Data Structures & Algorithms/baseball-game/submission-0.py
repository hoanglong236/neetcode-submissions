class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        res = 0
        for op in operations:
            if op == '+':
                n1 = stack.pop()
                n2 = stack[-1]
                total = n1 + n2
                stack.append(n1)
                stack.append(total)
                res += total
            elif op == 'D':
                d = stack[-1]
                stack.append(d * 2)
                res += d * 2
            elif op == 'C':
                res -= stack.pop()
            else:
                d = int(op)
                stack.append(d)
                res += d
        return res
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = 0
        stack = []
        for op in operations:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
                ans += stack[-1]
            elif op == 'D':
                stack.append(stack[-1] * 2)
                ans += stack[-1]
            elif op == 'C':
                ans -= stack.pop()
            else:
                stack.append(int(op))
                ans += stack[-1]
        return ans
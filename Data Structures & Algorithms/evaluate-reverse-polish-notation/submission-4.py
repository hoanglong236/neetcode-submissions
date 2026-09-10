class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t == '+':
                tmp = stack.pop()
                stack[-1] += tmp
            elif t == '-':
                tmp = stack.pop()
                stack[-1] -= tmp
            elif t == '*':
                tmp = stack.pop()
                stack[-1] *= tmp
            elif t == '/':
                tmp = stack.pop()
                res = abs(stack[-1]) // abs(tmp)
                stack[-1] = -res if (stack[-1] < 0) ^ (tmp < 0) else res
            else:
                stack.append(int(t))
        return stack.pop()
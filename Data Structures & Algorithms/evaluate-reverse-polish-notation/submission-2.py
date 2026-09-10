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
                stack[-1] = int(stack[-1] / tmp)
            else:
                stack.append(int(t))
        return stack.pop()
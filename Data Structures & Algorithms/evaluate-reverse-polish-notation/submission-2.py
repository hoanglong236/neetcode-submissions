class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for t in tokens:
            if t.isdigit():
                operands.append(int(t))
            elif t[0] == '-' and t[1:].isdigit():
                operands.append(-int(t[1:]))
            else:
                o1, o2 = operands.pop(), operands.pop()
                if t == '+':
                    operands.append(o2 + o1)
                elif t == '-':
                    operands.append(o2 - o1)
                elif t == '*':
                    operands.append(o2 * o1)
                elif t == '/':
                    operands.append(int(o2 / o1))
        return operands.pop()
class Solution:
    def decodeString(self, s: str) -> str:
        decoded = []
        stack_ch, stack_num = [], []
        num = 0

        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == '[':
                stack_ch.append([])
                stack_num.append(num)
                num = 0
            elif ch == ']':
                seq = ''.join(stack_ch.pop()) * stack_num.pop()
                if stack_ch:
                    stack_ch[-1].append(seq)
                else:
                    decoded.append(seq)
            elif stack_ch:
                stack_ch[-1].append(ch)
            else:
                decoded.append(ch)
        return ''.join(decoded)
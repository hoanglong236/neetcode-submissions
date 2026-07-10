class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        seq = ['/']
        for ch in path:
            if ch == '/':
                if seq[-1] == '/':
                    continue
                name = ''.join(seq)
                if name == '/.':
                    seq = []
                elif name == '/..':
                    if stack:
                        stack.pop()
                    seq = []
                else:
                    stack.append(name)
                    seq = []
            seq.append(ch)
            print(stack, seq)

        name = ''.join(seq)
        if name == '/..':
            if stack:
                stack.pop()
        elif name == '/.':
            pass
        elif name == '/':
            pass
        else:
            stack.append(name)
        return ''.join(stack) if stack else '/'
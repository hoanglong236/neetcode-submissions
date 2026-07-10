class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        seq = ['/']
        for ch in path:
            if ch == '/':
                name = ''.join(seq)
                if name == '/..':
                    if stack:
                        stack.pop()
                elif name != '/' and name != '/.':
                    stack.append(name)
                seq = []
            seq.append(ch)
            print(stack, seq)

        name = ''.join(seq)
        if name == '/..':
            if stack:
                stack.pop()
        elif name != '/.' and name != '/':
            stack.append(name)
        return ''.join(stack) if stack else '/'
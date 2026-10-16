class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        seq = []
        for i in range(n + 1):
            if i == n or path[i] == '/':
                folder = ''.join(seq)
                if folder == '..':
                    if stack:
                        stack.pop()
                elif folder and folder != '.':
                    stack.append(folder)
                seq = []
            else:
                seq.append(path[i])
        return '/' + '/'.join(stack)
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        seq = []
        for i, ch in enumerate(path):
            sub_folder = ''
            if ch != '/':
                seq.append(ch)
            if i == len(path) - 1 or (ch == '/' and seq):
                name = ''.join(seq)
                if name == '..':
                    if stack:
                        stack.pop()
                elif name != '.' and name != '/':
                    sub_folder = name
                seq = []

            if sub_folder:
                stack.append(sub_folder)
        return '/' + '/'.join(stack)
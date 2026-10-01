class Solution:
    def simplifyPath(self, path: str) -> str:
        n = len(path)
        stack = []
        folder_chars = []
        for i in range(n + 1):
            if i == n or path[i] == '/':
                if folder_chars:
                    folder = ''.join(folder_chars)
                    if folder != '.' and folder != '..':
                        stack.append(folder)
                    elif folder == '..' and stack:
                        stack.pop()
                    folder_chars = []
            else:
                folder_chars.append(path[i])
        return '/' + '/'.join(stack)
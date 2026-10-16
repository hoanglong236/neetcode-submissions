class Solution:
    def simplifyPath(self, path: str) -> str:
        partials = path.split('/')
        stack = []
        for folder in partials:
            if folder == '..':
                if stack:
                    stack.pop()
            elif folder != '' and folder != '.':
                stack.append(folder)
        return '/' + '/'.join(stack)
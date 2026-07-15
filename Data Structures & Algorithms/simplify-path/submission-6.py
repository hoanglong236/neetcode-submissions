class Solution:
    def simplifyPath(self, path: str) -> str:
        canonical = ['/']
        for ch in path:
            if not (ch == '/' and canonical[-1] == '/'):
                canonical.append(ch)
        canonical = ''.join(canonical)
        ans = []
        for folder in canonical.split('/'):
            if folder == '..':
                if ans:
                    ans.pop()
            elif folder and folder != '.':
                ans.append(folder)
        return '/' + '/'.join(ans)
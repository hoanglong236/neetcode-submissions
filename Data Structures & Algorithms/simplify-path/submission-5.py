class Solution:
    def simplifyPath(self, path: str) -> str:
        folders = []
        name = []
        for ch in path:
            if ch == '/':
                seq = ''.join(name)
                if seq:
                    if seq == '..':
                        if folders:
                            folders.pop()
                    elif seq != '.':
                        folders.append(seq)
                name = []
            else:
                name.append(ch)

        seq = ''.join(name)
        if seq:
            if seq == '..':
                if folders:
                    folders.pop()
            elif seq != '.':
                folders.append(seq)
        return '/' + '/'.join(folders)
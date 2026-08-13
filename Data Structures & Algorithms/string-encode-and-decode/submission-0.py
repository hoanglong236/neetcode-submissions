class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join((str(len(s)) + '*' + s for s in strs))

    def decode(self, s: str) -> List[str]:
        res, i, size = [], 0, 0
        while i < len(s):
            if s[i] != '*':
                size = size * 10 + int(s[i])
                i += 1
            else:
                res.append(s[i + 1:i + size + 1])
                i += size + 1
                size = 0
        return res
class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join([str(len(s)) + "." + s for s in strs])

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        j = 0
        while j < len(s):
            if s[j] == '.':
                s_len = int(s[i:j])
                i = j + 1
                j = j + 1 + s_len
                ans.append(s[i: j])
                i = j
            else:
                j += 1
        return ans

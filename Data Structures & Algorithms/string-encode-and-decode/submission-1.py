class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(".".join([str(len(s)), s]))
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        s_len_start = 0
        i = 0
        while i < len(s):
            if s[i] == '.':
                s_len = int(s[s_len_start:i])
                ans.append(s[i + 1: i + s_len + 1])
                i += s_len
                s_len_start = i + 1
            i += 1
        return ans

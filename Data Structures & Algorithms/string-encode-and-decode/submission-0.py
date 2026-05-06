class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = []
        for s in strs:
            ans.append(".".join([str(len(s)), s]))
        return "".join(ans)

    def decode(self, s: str) -> List[str]:
        ans = []
        s_len_idx = 0
        for i in range(len(s)):
            if s[i] == '.':
                s_len = int(s[s_len_idx:i])
                ans.append(s[i + 1: i + s_len + 1])
                s_len_idx = i + s_len + 1
                i += s_len
        return ans

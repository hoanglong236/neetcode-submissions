class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]
        prefix_len = len(ans)
        for i in range(1, len(strs)):
            if strs[i] == '':
                return ''
            prefix_len = min(len(strs[i]), prefix_len)
            while strs[i][:prefix_len] != ans[:prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ''
        return ''.join(ans[:prefix_len])

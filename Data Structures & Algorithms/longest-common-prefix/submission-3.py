class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for prefix_idx in range(len(strs[0])):
            base_ch = strs[0][prefix_idx]
            for j in range(1, len(strs)):
                if len(strs[j]) == prefix_idx or strs[j][prefix_idx] != base_ch:
                    return strs[0][:prefix_idx]
        return strs[0]

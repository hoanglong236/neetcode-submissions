class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res, candidate = 0, 0
        for i, ch in enumerate(s):
            if ch in seen:
                candidate = max(candidate, seen[ch] + 1)
            seen[ch] = i
            res = max(res, i - candidate + 1)
        return res
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res, candidate = 0, 0
        for i, ch in enumerate(s):
            last_seen = seen.get(ch, -1)
            if last_seen >= candidate:
                candidate = last_seen + 1
            seen[ch] = i
            res = max(res, i - candidate + 1)
        return res
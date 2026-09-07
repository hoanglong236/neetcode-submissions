class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        res, window_start = 0, 0
        for i, ch in enumerate(s):
            last_seen = seen.get(ch, -1)
            if window_start <= last_seen:
                res = max(res, i - window_start)
                window_start = last_seen + 1
            seen[ch] = i
        return max(res, len(s) - window_start)
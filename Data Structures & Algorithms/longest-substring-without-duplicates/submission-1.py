class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, pivot = 0, 0
        last_seen = {}

        for i, ch in enumerate(s):
            last_idx = last_seen.get(ch, -1)
            if last_idx > -1 and pivot <= last_idx:
                ans = max(i - pivot, ans)
                pivot = last_idx + 1
            last_seen[ch] = i

        return max(ans, len(s) - pivot)
                
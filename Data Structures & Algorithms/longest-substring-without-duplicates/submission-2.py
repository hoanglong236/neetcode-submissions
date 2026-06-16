class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans, start = 0, 0
        seen = {}
        for end in range(len(s)):
            if s[end] in seen:
                if seen[s[end]] >= start:
                    start = seen[s[end]] + 1
            seen[s[end]] = end
            ans = max(ans, end - start + 1)
        return ans
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, start = 0, 0
        window_freq = {}
        for end in range(len(s)):
            window_freq[ord(s[end])] = window_freq.get(ord(s[end]), 0) + 1
            if end - start + 1 > max(window_freq.values()) + k:
                window_freq[ord(s[start])] -= 1
                start += 1
            else:
                ans = max(ans, end - start + 1)
        return ans
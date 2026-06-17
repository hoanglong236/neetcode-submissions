class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, start, most = 0, 0, 0
        window_freq = {}
        for end in range(len(s)):
            window_freq[ord(s[end])] = window_freq.get(ord(s[end]), 0) + 1
            most = max(most, window_freq[ord(s[end])])
            if end - start + 1 > most + k:
                window_freq[ord(s[start])] -= 1
                start += 1
            else:
                ans = max(ans, end - start + 1)
        return ans
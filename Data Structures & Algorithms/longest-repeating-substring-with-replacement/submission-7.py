class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, start = 0, 0
        window_freq = [0] * 26
        for end in range(len(s)):
            window_freq[ord(s[end]) - ord('A')] += 1
            most = max(window_freq)
            if end - start + 1 > most + k:
                window_freq[ord(s[start]) - ord('A')] -= 1
                start += 1
            ans = max(ans, end - start + 1)
        return ans
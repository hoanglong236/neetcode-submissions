class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start, most = 0, 0
        window_freq = [0] * 26
        for end in range(len(s)):
            window_freq[ord(s[end]) - 65] += 1
            most = max(most, window_freq[ord(s[end]) - 65])
            if end - start + 1 > most + k:
                window_freq[ord(s[start]) - 65] -= 1
                start += 1
        return len(s) - start
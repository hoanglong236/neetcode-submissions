class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        start, end, most = 0, 0, 0
        while end < len(s):
            ch_freq = freq.get(s[end], 0) + 1
            if ch_freq > most:
                most = ch_freq
            freq[s[end]] = ch_freq

            end += 1
            if end - start - most > k:
                freq[s[start]] -= 1
                start += 1
        return min(most + k, len(s))
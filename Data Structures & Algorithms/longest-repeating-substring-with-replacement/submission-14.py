class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, start = 0, 0
        freq = [0] * 26
        most = 0
        for end in range(len(s)):
            o = ord(s[end]) - 65
            freq[o] += 1
            most = max(most, freq[o])
            if end - start + 1 > most + k:
                freq[ord(s[start]) - 65] -= 1
                start += 1
        return end - start + 1
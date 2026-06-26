class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans, start = 0, 0
        freq = [0] * 26
        most = 0
        for end in range(len(s)):
            freq[ord(s[end]) - 65] += 1
            if end - start + 1 > max(freq) + k:
                freq[ord(s[start]) - 65] -= 1
                start += 1
        return end - start + 1
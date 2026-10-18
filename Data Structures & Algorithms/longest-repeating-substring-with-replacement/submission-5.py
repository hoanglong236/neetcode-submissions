class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = [0] * 26
        most, start = 0, 0
        for i, ch in enumerate(s):
            freq[ord(ch) - ord('A')] += 1
            while max(freq) + k < i - start + 1:
                freq[ord(s[start]) - ord('A')] -= 1
                start += 1
            most = max(most, max(freq) + k)
        return min(most, len(s))
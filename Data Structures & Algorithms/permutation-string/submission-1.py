class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n2 < n1:
            return False

        freq = [0] * 26
        for ch in s1:
            freq[ord(ch) - 97] += 1

        freq2 = [0] * 26
        for idx, ch in enumerate(s2):
            freq2[ord(ch) - 97] += 1

            if idx >= n1 - 1:
                if freq == freq2:
                    return True
                freq2[ord(s2[idx - n1 + 1]) - 97] -= 1
        return False
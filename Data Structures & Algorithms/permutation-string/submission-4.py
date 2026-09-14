class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        freq1 = [0] * 26
        base_ch_prefix = ord('a')
        for ch in s1:
            freq1[ord(ch) - base_ch_prefix] += 1

        freq2 = [0] * 26
        start = 0
        for i, ch in enumerate(s2):
            freq2[ord(ch) - base_ch_prefix] += 1
            if i >= n1:
                freq2[ord(s2[start]) - base_ch_prefix] -= 1
                start += 1
            if freq1 == freq2:
                return True
        return False
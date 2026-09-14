class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False

        freq1 = [0] * 26
        base_ch_ord = ord('a')
        for ch in s1:
            freq1[ord(ch) - base_ch_ord] += 1

        freq2 = [0] * 26
        start, count = 0, 0
        for i in range(n2):
            o = ord(s2[i]) - base_ch_ord
            if freq1[o] > 0:
                if freq2[o] < freq1[o]:
                    count += 1
                freq2[o] += 1
            if i >= n1:
                o_start = ord(s2[start]) - base_ch_ord
                if freq1[o_start] > 0:
                    if freq2[o_start] <= freq1[o_start]:
                        count -= 1
                    freq2[o_start] -= 1
                start += 1
            if count == n1:
                return True
        return False
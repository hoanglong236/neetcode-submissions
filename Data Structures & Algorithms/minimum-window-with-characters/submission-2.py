class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ""

        freq_t = [0] * 128
        for ch in t:
            freq_t[ord(ch)] += 1

        res_start, res_end = 0, n1
        w_start, count = 0, 0
        freq_s = [0] * 128
        for w_end in range(n1):
            o_end = ord(s[w_end])
            freq_s[o_end] += 1
            if freq_s[o_end] <= freq_t[o_end]:
                count += 1
            while count == n2:
                if res_end - res_start > w_end - w_start:
                    res_start, res_end = w_start, w_end
                o_start = ord(s[w_start])
                freq_s[o_start] -= 1
                if freq_s[o_start] < freq_t[o_start]:
                    count -= 1
                w_start += 1
        if res_end == n1:
            return ""
        return s[res_start:res_end + 1]
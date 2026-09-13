from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n1, n2 = len(s), len(t)
        if n1 < n2:
            return ""

        freq_t = defaultdict(int)
        for ch in t:
            freq_t[ch] += 1

        res_start, res_end = 0, n1
        w_start, w_end = 0, 0
        count = 0
        freq_s = defaultdict(int)
        while w_end < n1:
            freq_s[s[w_end]] += 1
            if freq_s[s[w_end]] <= freq_t[s[w_end]]:
                count += 1
            while count == n2:
                if res_end - res_start > w_end - w_start:
                    res_start, res_end = w_start, w_end
                freq_s[s[w_start]] -= 1
                if freq_s[s[w_start]] < freq_t[s[w_start]]:
                    count -= 1
                w_start += 1
            w_end += 1
        if res_end == len(s):
            return ""
        return s[res_start:res_end + 1]
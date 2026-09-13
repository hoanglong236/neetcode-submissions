from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = defaultdict(int)
        for ch in t:
            freq_t[ch] += 1
        
        res_start, res_end = 0, len(s)
        w_start, w_end = 0, 0
        freq_s = defaultdict(int)
        while w_end < len(s):
            freq_s[s[w_end]] += 1
            while True:
                is_valid = True
                for k, v in freq_t.items():
                    if v > freq_s[k]:
                        is_valid = False
                        break
                if is_valid:
                    if res_end - res_start > w_end - w_start:
                        res_start, res_end = w_start, w_end
                    freq_s[s[w_start]] -= 1
                    w_start += 1
                else:
                    break
            w_end += 1
        if res_end == len(s):
            return ""
        return s[res_start:res_end + 1]
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''

        freq_t = [0] * 128
        for ch in t:
            freq_t[ord(ch)] += 1

        filtered_s = [(i, ord(ch)) for i, ch in enumerate(s) if freq_t[ord(ch)] > 0]
        if not filtered_s:
            return ''

        ans = (0, len(s))
        start, remain = 0, len(t) 
        for i, o in filtered_s:
            if freq_t[o] > 0:
                remain -= 1
            freq_t[o] -= 1
            while remain == 0:
                i_start, o_start = filtered_s[start]
                if ans[1] - ans[0] > i - i_start:
                    ans = (i_start, i)
                freq_t[o_start] += 1
                if freq_t[o_start] > 0:
                    remain += 1
                start += 1
        return s[ans[0]:ans[1] + 1] if ans[1] < len(s) else ''
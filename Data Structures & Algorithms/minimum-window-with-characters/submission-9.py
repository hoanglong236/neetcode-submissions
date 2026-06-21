class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        ans = (0, len(s))
        start, end = 0, 0
        total = len(t)
        while end < len(s):
            if s[end] in freq_t:
                freq_t[s[end]] -= 1
                if freq_t[s[end]] >= 0:
                    total -= 1
            while total == 0:
                if end - start < ans[1] - ans[0]:
                    ans = (start, end)
                if s[start] in freq_t:
                    freq_t[s[start]] += 1
                    if freq_t[s[start]] > 0:
                        total += 1
                if start < end:
                    start += 1
                else:
                    end += 1
            end += 1
        if ans[1] == len(s):
            return ""
        return s[ans[0]:ans[1] + 1]
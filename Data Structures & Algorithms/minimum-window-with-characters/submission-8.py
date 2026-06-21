class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        ans = (0, len(s))
        start, end = 0, 0
        freq = {ch: count for ch, count in freq_t.items()}
        total = len(t)
        while end < len(s):
            if s[end] in freq_t:
                freq[s[end]] -= 1
                if freq[s[end]] >= 0:
                    total -= 1
            while total == 0:
                print("start", start, end, total, freq)
                if end - start + 1 < ans[1] - ans[0] + 1:
                    ans = (start, end)
                if s[start] in freq_t:
                    freq[s[start]] += 1
                    if freq[s[start]] > 0:
                        total += 1
                if start < end:
                    start += 1
                else:
                    end += 1
                print("end", start, end, total, freq)
            end += 1
        if ans[1] == len(s):
            return ""
        return s[ans[0]:ans[1] + 1]
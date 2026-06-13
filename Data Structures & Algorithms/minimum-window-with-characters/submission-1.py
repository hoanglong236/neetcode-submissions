class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        shortest = [0, len(s)]
        start, end = 0, 0
        freq_window = {}
        while end < len(s):
            freq_window[s[end]] = freq_window.get(s[end], 0) + 1
            is_contain = True
            for ch, count in freq_t.items():
                if ch not in freq_window or count > freq_window[ch]:
                    is_contain = False
                    break
            if is_contain:
                if shortest[1] - shortest[0] > end - start:
                    shortest = [start, end]

                freq_window[s[start]] -= 1
                freq_window[s[end]] -= 1
                start += 1
            else:
                end += 1
        if shortest[1] == len(s):
            return ""
        return s[shortest[0]:shortest[1] + 1]
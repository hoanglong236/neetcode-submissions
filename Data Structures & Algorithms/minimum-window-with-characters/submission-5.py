class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        freq_t = {}
        for ch in t:
            freq_t[ch] = freq_t.get(ch, 0) + 1

        shortest = [0, len(s)]
        start = 0
        freq_window = {}
        valid_window = True 
        for end in range(len(s)):
            freq_window[s[end]] = freq_window.get(s[end], 0) + 1
            if freq_window[s[end]] != freq_t.get(s[end]):
                continue
            valid_window = True
            for ch, count in freq_t.items():
                if ch not in freq_window or count > freq_window[ch]:
                    valid_window = False
                    break
            if valid_window:
                break
        if not valid_window:
            return ""
        freq_window[s[end]] -= 1
        for end in range(end, len(s)):
            freq_window[s[end]] = freq_window.get(s[end], 0) + 1
            if s[end] in freq_t:
                while freq_window[s[start]] > freq_t.get(s[start], 0):
                    freq_window[s[start]] -= 1
                    start += 1
                if shortest[1] - shortest[0] > end - start:
                    shortest = [start, end]

        if shortest[1] == len(s):
            return ""
        return s[shortest[0]:shortest[1] + 1]
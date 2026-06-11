class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {s[0]: 1}
        ans = 0
        most = 1
        start, end, window_size = 0, 1, 1
        while end < len(s):
            if s[end] in freq:
                ch_freq = freq[s[end]] + 1
                if ch_freq > most:
                    most = ch_freq
                freq[s[end]] = ch_freq
            else:
                freq[s[end]] = 1
                # print(freq)
            
            end += 1
            window_size += 1
            if most + k < window_size:
                freq[s[start]] -= 1
                start += 1
                window_size -= 1
                most = max(freq.values())
                # print(s[start])
                # print(freq, most, end, window_size)
            ans = max(ans, most)
            # print(freq, most, end, window_size)
        return min(ans + k, len(s))
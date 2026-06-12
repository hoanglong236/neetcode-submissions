class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_s1 = [0] * 26
        for ch in s1:
            freq_s1[ord(ch) - ord('a')] += 1
        window_size = len(s1)

        freq_window = [0] * 26
        start = 0
        for end in range(len(s2)):
            freq_window[ord(s2[end]) - ord('a')] += 1
            if freq_window == freq_s1:
                return True

            if end - start + 1 >= window_size:
                freq_window[ord(s2[start]) - ord('a')] -= 1
                start += 1
        return False
                
            


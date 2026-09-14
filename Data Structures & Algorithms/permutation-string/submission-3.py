class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        freq1 = [0] * 26
        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        
        freq2 = [0] * 26
        seen = [[] for _ in range(26)]
        start, end = 0, 0
        while end < n2:
            end_ch_idx = ord(s2[end]) - ord('a')
            if freq1[end_ch_idx] == 0:
                start += 1
                end += 1
                seen = [[] for _ in range(26)]
                freq2 = [0] * 26
                continue
            if freq2[end_ch_idx] >= freq1[end_ch_idx]:
                start = seen[end_ch_idx][0] + 1
                end = start
                seen = [[] for _ in range(26)]
                freq2 = [0] * 26
                continue
            freq2[end_ch_idx] += 1
            if freq1 == freq2:
                return True
            seen[end_ch_idx].append(end)
            end += 1
            if end - start + 1 == n1:
                start += 1
            # print(start, end, freq2, seen)
        return False
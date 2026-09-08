class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = [''] * (n1 + n2)
        count = 0
        n = min(n1, n2)
        for i in range(n):
            res[count] = word1[i]
            res[count + 1] = word2[i]
            count += 2
        res[count:] = word1[n:] if n == n2 else word2[n:]
        return ''.join(res)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = [''] * (n1 + n2)
        n = min(n1, n2)
        res[0:2 * n - 1:2] = word1[:n]
        res[1:2 * n:2] = word2[:n]
        res[2 * n:] = word1[n:] + word2[n:]
        return ''.join(res)
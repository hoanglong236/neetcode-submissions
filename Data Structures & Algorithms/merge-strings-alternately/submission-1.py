class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = [''] * (n1 + n2)
        if n1 <= n2:
            res[0:2 * n1 - 1:2] = word1[:]
            res[1:2 * n1:2] = word2[:n1]
            res[2 * n1:] = word2[n1:]
        else:
            res[0:2 * n2 - 1:2] = word1[:n2]
            res[1:2 * n2:2] = word2[:]
            res[2 * n2:] = word1[n2:]
        return ''.join(res)
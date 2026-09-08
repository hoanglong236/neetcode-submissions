class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        res = [''] * (n1 + n2)
        count = 0
        for i in range(n1):
            res[count] = word1[i]
            count += 1
            if i >= n2:
                break
            res[count] = word2[i]
            count += 1
        if i < n1 - 1:
            res[count:] = word1[i + 1:]
        else:
            res[count:] = word2[i + 1:]
        return ''.join(res)
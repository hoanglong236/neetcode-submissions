class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = [''] * (len(word1) + len(word2))
        count = 0
        for i in range(len(word1)):
            res[count] = word1[i]
            count += 1
            if i < len(word2):
                res[count] = word2[i]
                count += 1
        if i < len(word2):
            res[count:] = word2[i + 1:]
        return ''.join(res)
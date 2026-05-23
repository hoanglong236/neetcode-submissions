class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        n = min(n1, n2)
        ans = []
        for i in range(n):
            ans.append(word1[i])
            ans.append(word2[i])

        if n1 < n2:
            for i in range(n1, n2):
                ans.append(word2[i])
        else:
            for i in range(n2, n1):
                ans.append(word1[i])
        
        return ''.join(ans)
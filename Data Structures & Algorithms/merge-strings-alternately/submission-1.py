class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)
        ans = []
        for i in range(min(n1, n2)):
            ans.append(word1[i])
            ans.append(word2[i])

        ans.extend(word2[n1:n2] if n1 < n2 else word1[n2:n1])
        return ''.join(ans)
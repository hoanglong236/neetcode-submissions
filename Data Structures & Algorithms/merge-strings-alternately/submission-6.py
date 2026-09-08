from itertools import zip_longest

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join(x[0] + x[1] for x in zip_longest(word1, word2, fillvalue=''))
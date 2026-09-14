from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        counter1 = Counter(s1)
        for i in range(n2 - n1 + 1):
            counter2 = Counter(s2[i:i + n1])
            if counter2 == counter1:
                return True
        return False
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                s1 = s[left:right]
                if s1 == s1[::-1]:
                    return True
                s2 = s[left + 1: right + 1]
                return s2 == s2[::-1]
        return True
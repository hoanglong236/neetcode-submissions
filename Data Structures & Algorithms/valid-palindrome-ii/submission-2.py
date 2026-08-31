class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                if s[left] != s[right - 1] and s[left + 1] != s[right]:
                    return False
                tmp = s[left:right]
                if tmp == tmp[::-1]:
                    return True
                tmp = s[left + 1: right + 1]
                return tmp == tmp[::-1]
        return True
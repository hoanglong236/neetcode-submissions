class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                skip_left = s[l + 1: r + 1]
                if skip_left == skip_left[::-1]:
                    return True
                else:
                    skip_right = s[l: r]
                    return skip_right == skip_right[::-1]
            l += 1
            r -= 1
        return True
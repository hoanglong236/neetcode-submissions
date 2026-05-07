class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum_chars = []
        for ch in s.lower():
            if ch.isalnum():
                alnum_chars.append(ch)
        l, r = 0, len(alnum_chars) - 1
        while l < r:
            if alnum_chars[l] != alnum_chars[r]:
                return False
            l += 1
            r -= 1
        return True
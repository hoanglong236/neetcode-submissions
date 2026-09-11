class Solution:
    def isValid(self, s: str) -> bool:
        close_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch not in close_parentheses:
                stack.append(ch)
            elif not stack or close_parentheses[ch] != stack.pop():
                return False
        return not stack
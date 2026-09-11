class Solution:
    def isValid(self, s: str) -> bool:
        close_parentheses = {')': '(', ']': '[', '}': '{'}
        stack = []
        for ch in s:
            if ch in close_parentheses:
                if not stack or close_parentheses[ch] != stack.pop():
                    return False
                continue
            stack.append(ch)
        return not stack
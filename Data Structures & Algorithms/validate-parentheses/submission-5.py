class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'()', '[]', '{}'}
        stack = []
        for ch in s:
            if ch == ')' or ch == ']' or ch == '}':
                if not stack or stack.pop() + ch not in parentheses:
                    return False
                continue
            stack.append(ch)
        return not stack
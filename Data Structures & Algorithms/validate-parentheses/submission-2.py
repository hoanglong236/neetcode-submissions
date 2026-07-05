class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {'[': ']', '(': ')', '{': '}'}
        for ch in s:
            if ch == '[' or ch == '(' or ch == '{':
                stack.append(ch)
            elif not stack or pairs[stack.pop()] != ch:
                return False
        return not stack
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and stack[-1] > 0 and stack[-1] < -ast:
                stack.pop()
            if not stack or not (stack[-1] > 0 and ast < 0):
                stack.append(ast)
            elif stack[-1] == -ast:
                stack.pop()
        return stack
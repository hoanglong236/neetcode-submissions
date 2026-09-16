class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            is_add = True
            while stack and stack[-1] > 0 and ast < 0:
                if stack[-1] < -ast:
                    stack.pop()
                else:
                    if stack[-1] == -ast:
                        stack.pop()
                    is_add = False
                    break
            if is_add:
                stack.append(ast)
        return stack
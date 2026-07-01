class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                cur_size = abs(ast)
                is_add = True
                while stack and stack[-1] > 0:
                    if cur_size > stack[-1]:
                        stack.pop()
                    elif cur_size == stack[-1]:
                        stack.pop()
                        is_add = False
                        break
                    else:
                        is_add = False
                        break
                if is_add:
                    stack.append(ast)

        return stack
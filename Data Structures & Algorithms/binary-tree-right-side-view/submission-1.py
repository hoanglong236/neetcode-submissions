# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = [(0, root)] if root else []
        while stack:
            level, node = stack.pop()
            if node.left:
                stack.append((level + 1, node.left))
            if node.right:
                stack.append((level + 1, node.right))
            if level == len(res):
                res.append(node.val)
                level += 1
        return res
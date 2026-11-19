# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0
        stack = [(1, root)] if root else []
        while stack:
            depth, node = stack.pop()
            if node.left:
                stack.append((depth + 1, node.left))
            if node.right:
                stack.append((depth + 1, node.right))
            max_depth = max(max_depth, depth)
        return max_depth
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        prev, node = None, root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if prev is node.right or node.right is None:
                stack.pop()
                res.append(node.val)
                prev, node = node, None
            else:
                prev, node = node, node.right
        return res
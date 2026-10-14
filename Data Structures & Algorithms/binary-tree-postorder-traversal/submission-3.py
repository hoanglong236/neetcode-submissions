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
        node, last = root, None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            top = stack[-1]
            if top.right and top.right != last:
                node = top.right
            else:
                last = stack.pop()
                res.append(last.val)
        return res
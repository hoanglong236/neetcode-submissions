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
        node, last_visited = root, None
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right is last_visited:
                node = stack.pop()
                res.append(node.val)
                last_visited, node = node, None
            else:
                node = node.right
        return res
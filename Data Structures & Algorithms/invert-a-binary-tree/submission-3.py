# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            new_left = None
            new_right = None
            if node.right:
                new_left = dfs(node.right)
            if node.left:
                new_right = dfs(node.left)
            node.left = new_left
            node.right = new_right
            return node

        if root:
            return dfs(root)
        return None
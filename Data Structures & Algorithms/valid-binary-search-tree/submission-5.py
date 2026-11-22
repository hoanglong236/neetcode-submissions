# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float('-inf')

        def dfs(node):
            nonlocal prev
            if node.left and not dfs(node.left):
                return False
            if node.val <= prev:
                return False
            prev = node.val
            if node.right and not dfs(node.right):
                return False
            return True

        if root:
            return dfs(root)
        return True
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            good = False
            if node.val >= max_val:
                good = True
                max_val = node.val
            count = 1 if good else 0
            if node.left:
                count += dfs(node.left, max_val)
            if node.right:
                count += dfs(node.right, max_val)
            return count
        if root:
            return dfs(root, root.val)
        return 0
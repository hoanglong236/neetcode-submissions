# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            count = 0
            if node.val >= max_val:
                count = 1
                max_val = node.val
            if node.left:
                count += dfs(node.left, max_val)
            if node.right:
                count += dfs(node.right, max_val)
            return count
        if root:
            return dfs(root, root.val)
        return 0
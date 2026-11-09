# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, min_val, max_val):
            if node.val <= min_val or node.val >= max_val:
                return False
            res = True
            if node.left:
                res = dfs(node.left, min_val, min(max_val, node.val))
            if not res:
                return False
            if node.right:
                res = dfs(node.right, max(min_val, node.val), max_val)
            return res
        if root:
            return dfs(root, float('-inf'), float('inf'))
        return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, nearest_left, nearest_right):
            if node.val <= nearest_left or node.val >= nearest_right:
                return False
            if node.left:
                if not dfs(node.left, nearest_left, min(nearest_right, node.val)):
                    return False
            if node.right:
                return dfs(node.right, max(nearest_left, node.val), nearest_right)
            return True

        if root:
            return dfs(root, float('-inf'), float('inf'))
        return False
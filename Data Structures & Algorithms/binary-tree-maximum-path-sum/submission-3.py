# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        def dfs(node):
            nonlocal max_sum
            left_path = max(0, dfs(node.left)) if node.left else 0
            right_path = max(0, dfs(node.right)) if node.right else 0
            max_sum = max(max_sum, node.val + left_path + right_path)
            return node.val + max(left_path, right_path)

        if root:
            dfs(root)
        return max_sum
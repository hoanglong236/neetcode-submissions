# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        target = TreeNode(val)
        
        def dfs(node):
            if node is None:
                return target
            if node.val > val:
                node.left = dfs(node.left)
            else:
                node.right = dfs(node.right)
            return node

        return dfs(root)
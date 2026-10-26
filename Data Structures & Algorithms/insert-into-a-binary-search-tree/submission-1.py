# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        target = TreeNode(val)
        if root is None:
            return target
        parent, node = None, root
        while node:
            parent = node
            node = node.left if node.val > val else node.right
        if parent.val > val:
            parent.left = target
        else:
            parent.right = target
        return root
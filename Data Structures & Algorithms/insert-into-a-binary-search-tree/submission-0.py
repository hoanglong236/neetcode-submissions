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
        node = root
        while node:
            if node.val > val:
                if node.left is None:
                    node.left = target
                    break
                node = node.left
            else:
                if node.right is None:
                    node.right = target
                    break
                node = node.right
        return root
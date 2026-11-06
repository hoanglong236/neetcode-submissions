# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node = None, root
        while node:
            if node.val == key:
                break
            parent = node
            if node.val < key:
                node = node.right
            else:
                node = node.left
        if node is None:
            return root

        if node.left is None:
            if parent is None:
                return node.right
            if parent.val < node.val:
                parent.right = node.right
            else:
                parent.left = node.right
            return root

        replace_parent, replace = node, node.left
        while replace.right:
            replace_parent, replace = replace, replace.right
        if replace_parent is node:
            replace_parent.left = replace.left
        else:
            replace_parent.right = replace.left

        replace.left, replace.right = node.left, node.right
        if parent is None:
            return replace
        if parent.val < replace.val:
            parent.right = replace
        else:
            parent.left = replace
        return root
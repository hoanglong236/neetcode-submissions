# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(0, root)
        is_left = True
        parent, node = dummy, root
        while node:
            if node.val == key:
                break
            is_left = node.val > key
            parent = node
            node = node.left if is_left else node.right
        if node is None:
            return dummy.left

        if node.left is None:
            if is_left:
                parent.left = node.right
            else:
                parent.right = node.right
            return dummy.left

        replacement_parent, replacement = node, node.left
        while replacement.right:
            replacement_parent, replacement = replacement, replacement.right
        if replacement_parent is node:
            replacement_parent.left = replacement.left
        else:
            replacement_parent.right = replacement.left

        replacement.left, replacement.right = node.left, node.right
        if is_left:
            parent.left = replacement
        else:
            parent.right = replacement
        return dummy.left
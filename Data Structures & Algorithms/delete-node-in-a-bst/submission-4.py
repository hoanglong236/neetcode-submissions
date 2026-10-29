# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        parent, node = None, root
        is_left = False
        while node:
            if node.val == key:
                break
            parent = node
            is_left = node.val > key
            node = node.left if is_left else node.right
        if node is None:
            return root

        nearest = None
        if node.left:
            parent_nearest, nearest = node, node.left
            while nearest.right:
                parent_nearest, nearest = nearest, nearest.right
            if parent_nearest is node:
                parent_nearest.left = nearest.left
            else:
                parent_nearest.right = nearest.left
        elif node.right:
            parent_nearest, nearest = node, node.right
            while nearest.left:
                parent_nearest, nearest = nearest, nearest.left
            if parent_nearest is node:
                parent_nearest.right = nearest.right
            else:
                parent_nearest.left = nearest.right

        if nearest:
            nearest.left = node.left
            nearest.right = node.right
        if not parent:
            return nearest
        if is_left:
            parent.left = nearest
        else:
            parent.right = nearest
        return root
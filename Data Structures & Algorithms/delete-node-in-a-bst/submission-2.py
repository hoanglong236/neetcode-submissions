# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None
        parent, node = None, root
        is_left = False
        while node:
            if node.val == key:
                break
            parent = node
            is_left = node.val > key
            if is_left:
                node = node.left
            else:
                node = node.right
        if node is None:
            return root
        parent_nearest, nearest = node, None
        if node.left:
            nearest = node.left
            while nearest.right:
                is_nearest_left = False
                parent_nearest, nearest = nearest, nearest.right
            if parent_nearest is not node:
                parent_nearest.right = nearest.left
            else:
                parent_nearest.left = None
            nearest.right = node.right
            nearest.left = node.left
        elif node.right:
            nearest = node.right
            while nearest.left:
                parent_nearest, nearest = nearest, nearest.left
            if parent_nearest is not node:
                parent_nearest.left = nearest.right
            else:
                parent_nearest.right = None
            nearest.left = node.left
            nearest.right = node.right
        else:
            pass
        if is_left:
            if parent:
                parent.left = nearest
            else:
                return nearest
        else:
            if parent:
                parent.right = nearest
            else:
                return nearest
        return root
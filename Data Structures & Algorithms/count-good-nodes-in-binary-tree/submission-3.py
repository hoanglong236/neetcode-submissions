# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        stack = [(root.val, root)] if root else []
        while stack:
            max_val, node = stack.pop()
            if max_val <= node.val:
                count += 1
                max_val = node.val
            if node.right:
                stack.append((max_val, node.right))
            if node.left:
                stack.append((max_val, node.left))
        return count
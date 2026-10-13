# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        stack = []
        node, sibling = root, None
        while node or stack:
            while node:
                stack.append((node, sibling))
                sibling = node.right
                node = node.left
            if sibling:
                node, sibling = sibling, None
            else:
                node, sibling = stack.pop()
                if node:
                    res.append(node.val)
                node, sibling = sibling, None
        return res
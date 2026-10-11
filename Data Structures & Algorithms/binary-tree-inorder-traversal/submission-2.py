# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        nodes = []
        curr = root
        while len(nodes) > 0 or (curr is not None):
            while curr:
                nodes.append(curr)
                curr = curr.left
            curr = nodes.pop()
            res.append(curr.val)
            curr = curr.right
        return res
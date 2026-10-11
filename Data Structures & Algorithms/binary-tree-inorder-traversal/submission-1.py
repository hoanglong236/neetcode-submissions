# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        nodes = [[root, False]]
        while nodes:
            curr, browse_child = nodes.pop()
            if curr is not None:
                if browse_child:
                    res.append(curr.val)
                else:
                    nodes.append([curr.right, False])
                    nodes.append([curr, True])
                    nodes.append([curr.left, False])
        return res
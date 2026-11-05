# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def dfs(node, level):
            if level < len(res):
                res[level].append(node.val)
            else:
                res.append([node.val])
            if node.left:
                dfs(node.left, level + 1)
            if node.right:
                dfs(node.right, level + 1)
        
        if root:
            dfs(root, 0)
        return res
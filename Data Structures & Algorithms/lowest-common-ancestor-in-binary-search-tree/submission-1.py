# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def find_ancestors(node):
            curr = root
            stack = []
            while curr:
                stack.append(curr)
                if curr.val == node.val:
                    return stack
                if curr.val > node.val:
                    curr = curr.left
                else:
                    curr = curr.right
            return []

        p_ancestors = find_ancestors(p)
        q_ancestors = find_ancestors(q)
        n = min(len(p_ancestors), len(q_ancestors))
        for i in range(n):
            if p_ancestors[i].val != q_ancestors[i].val:
                return p_ancestors[i - 1]
        return p_ancestors[n - 1]
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        def find_path(node):
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

        p_path = find_path(p)
        q_path = find_path(q)
        i, j = 0, 0
        while i < len(p_path) and j < len(q_path):
            if p_path[i] == q_path[j]:
                i += 1
                j += 1
            else:
                break
        return p_path[i - 1]
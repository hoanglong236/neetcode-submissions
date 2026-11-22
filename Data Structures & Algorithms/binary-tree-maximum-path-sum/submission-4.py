# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float('-inf')
        prev, node = None, root
        stack = []
        node_gain = {None: 0}
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack[-1]
            if node.right is None or node.right is prev:
                stack.pop()
                left_gain = max(0, node_gain[node.left])
                right_gain = max(0, node_gain[node.right])
                max_sum = max(max_sum, node.val + left_gain + right_gain)
                node_gain[node] = node.val + max(left_gain, right_gain)
                prev, node = node, None
            else:
                node = node.right
        return max_sum
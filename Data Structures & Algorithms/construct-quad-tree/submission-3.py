"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val=False, isLeaf=False, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def dfs(r, c, size):
            if size == 1:
                return Node(bool(grid[r][c]), True)

            half = size // 2
            top_left = dfs(r, c, half)
            top_right = dfs(r, c + half, half)
            bottom_left = dfs(r + half, c, half)
            bottom_right = dfs(r + half, c + half, half)
            if (
                top_left.val
                == top_right.val
                == bottom_left.val
                == bottom_right.val
            ) and (
                top_left.isLeaf
                and top_right.isLeaf
                and bottom_left.isLeaf
                and bottom_right.isLeaf
            ):
                return Node(top_left.val, True)
            return Node(
                top_left.val,
                False,
                top_left,
                top_right,
                bottom_left,
                bottom_right
            )

        return dfs(0, 0, len(grid))
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
        root = Node()
        n = len(grid)

        def dfs(row_start, col_start, row_end, col_end):
            print(row_start, col_start, row_end, col_end)
            same = True
            base_val = grid[row_start][col_start]
            for r in range(row_start, row_end + 1):
                for c in range(col_start, col_end + 1):
                    if grid[r][c] != base_val:
                        same = False
                        break
            if same:
                return Node(bool(base_val), True)
            node = Node(bool(base_val))
            row_mid = (row_start + row_end + 1) // 2
            col_mid = (col_start + col_end + 1) // 2
            if row_start == row_mid:
                node.topLeft = Node(bool(grid[row_start][col_start]), True)
                node.topRight = Node(bool(grid[row_start][col_end]), True)
                node.bottomLeft = Node(bool(grid[row_end][col_start]), True)
                node.bottomRight = Node(bool(grid[row_end][col_end]), True)
            else:
                node.topLeft = dfs(row_start, col_start, row_mid - 1, col_mid - 1)
                node.topRight = dfs(row_start, col_mid, row_mid - 1, col_end)
                node.bottomLeft = dfs(row_mid, col_start, row_end, col_mid - 1)
                node.bottomRight = dfs(row_mid, col_mid, row_end, col_end)
            return node

        return dfs(0, 0, n - 1, n - 1)
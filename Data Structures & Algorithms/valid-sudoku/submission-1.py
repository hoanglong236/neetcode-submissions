class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_rule = [set() for _ in range(9)]
        col_rule = [set() for _ in range(9)]
        box_rule = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_rule[r]:
                    return False
                row_rule[r].add(board[r][c])
                if board[r][c] in col_rule[c]:
                    return False
                col_rule[c].add(board[r][c])
                box_idx = (r // 3) * 3 + (c // 3)
                if board[r][c] in box_rule[box_idx]:
                    return False
                box_rule[box_idx].add(board[r][c])
        return True
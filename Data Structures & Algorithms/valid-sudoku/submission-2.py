class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_rules = [set() for _ in range(9)]
        col_rules = [set() for _ in range(9)]
        square_rules = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    continue
                if board[r][c] in row_rules[r]:
                    return False
                if board[r][c] in col_rules[c]:
                    return False
                square_idx = (r // 3) * 3 + (c // 3)
                if board[r][c] in square_rules[square_idx]:
                    return False

                row_rules[r].add(board[r][c])
                col_rules[c].add(board[r][c])
                square_rules[square_idx].add(board[r][c])
        return True
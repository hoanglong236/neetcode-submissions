class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box_check = {(i, j): set() for i in range(3) for j in range(3)}

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == '.':
                    continue
                num = board[r][c]
                if num in row_check[r]:
                    return False
                row_check[r].add(num)
                if num in col_check[c]:
                    return False
                col_check[c].add(num)
                if num in box_check[(r // 3, c // 3)]:
                    return False
                box_check[(r // 3, c // 3)].add(num)
        return True
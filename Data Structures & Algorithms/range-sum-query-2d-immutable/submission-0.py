class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.prefix = [[[0] for _ in range(n)] for _ in range(m)]
        for r in range(m):
            for c in range(n):
                self.prefix[r][c] = matrix[r][c]
                if r > 0:
                    self.prefix[r][c] += self.prefix[r - 1][c]
                if c > 0:
                    self.prefix[r][c] += self.prefix[r][c - 1]
                if r > 0 and c > 0:
                    self.prefix[r][c] -= self.prefix[r - 1][c - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = self.prefix[row2][col2]
        if row1 > 0:
            res -= self.prefix[row1 - 1][col2]
        if col1 > 0:
            res -= self.prefix[row2][col1 - 1]
        if row1 > 0 and col1 > 0:
            res += self.prefix[row1 - 1][col1 - 1]
        return res

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix_area = []
        n, m = len(matrix), len(matrix[0])
        self.prefix_area = [[[] for _ in range(m)] for _ in range(n)]

        self.prefix_area[0][0] = matrix[0][0]
        # Calculate the first row
        for j in range(1, m):
            self.prefix_area[0][j] = self.prefix_area[0][j - 1] + matrix[0][j]
        # Calculate the first col
        for i in range(1, n):
            self.prefix_area[i][0] = self.prefix_area[i - 1][0] + matrix[i][0]
        # Calculate other cells
        for i in range(1, n):
            for j in range(1, m):
                self.prefix_area[i][j] = (
                    matrix[i][j]
                    + self.prefix_area[i][j - 1]
                    + self.prefix_area[i - 1][j]
                    - self.prefix_area[i - 1][j - 1]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        area = self.prefix_area[row2][col2]
        if row1 == 0:
            if col1 == 0:
                return area
            return area - self.prefix_area[row2][col1 - 1]
        if col1 == 0:
            return area - self.prefix_area[row1 - 1][col2]
        return (
            area
            - self.prefix_area[row2][col1 - 1]
            - self.prefix_area[row1 - 1][col2]
            + self.prefix_area[row1 - 1][col1 - 1]
        )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
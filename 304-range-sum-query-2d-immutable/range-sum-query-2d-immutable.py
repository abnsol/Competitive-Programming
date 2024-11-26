class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])
        self.ps = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(1,rows + 1):
            for c in range(1,cols + 1):
                self.ps[r][c] = self.ps[r - 1][c] + self.ps[r][c - 1] + matrix[r - 1][c - 1] - self.ps[r - 1][c - 1]
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.ps[row2 + 1][col2 + 1] - self.ps[row1][col2 + 1]\
         - self.ps[row2 + 1][col1] + self.ps[row1][col1]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
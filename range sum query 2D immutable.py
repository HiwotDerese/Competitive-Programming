class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        column = len(matrix[0])
        self.sum = [[0] * (column + 1) for i in range(row + 1)]
        for i in range(row):
            prefix_sum = 0
            for j in range(column):
                prefix_sum += matrix[i][j]
                top = self.sum[i][j+1]
                self.sum[i+1][j+1] = prefix_sum + top

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 = row1 + 1
        col1 = col1 + 1
        row2 = row2 + 1
        col2 = col2 + 1
        total = self.sum[row2][col2]
        top = self.sum[row1-1][col2]
        left = self.sum[row2][col1-1]
        sub = self.sum[row1-1][col1-1]
        return total - top - left + sub
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
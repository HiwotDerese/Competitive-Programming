class Solution:
    def maxArea(self,row, col, grid):
        # print(row, col)
        if row >= self.n or col >= self.m or min(row, col) < 0 or (row, col) in self.visited or grid[row][col] == 0:
            return 0

        # if :
        #     return 0

        if grid[row][col] == 1:
            self.count += 1
            self.visited.add((row, col))

        self.maxArea(row, col + 1, grid)
        self.maxArea(row, col - 1, grid)
        self.maxArea(row + 1, col, grid)
        self.maxArea(row - 1, col, grid)

        self.max_ = max(self.max_, self.count)
        

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.count, self.max_, self.n, self.m, self.visited = 0, 0, len(grid), len(grid[0]), set()
        for row in range(self.n):
            # print(row)
            for col in range(self.m):
                self.count = 0
                if (row, col) not in self.visited:
                    self.maxArea(row, col, grid)

        return self.max_
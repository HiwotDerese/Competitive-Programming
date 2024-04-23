class Solution:

    def dfs(self, grid1, grid2, row, col, visited):
        if (row, col) in visited or min(row, col) < 0 or row >= self.m or col >= self.n or grid2[row][col] == 0:
            return 

        if grid1[row][col] == 0:
            self.subIsland = False
            return

        visited.add((row, col))

        self.dfs(grid1, grid2, row + 1, col, visited)
        self.dfs(grid1, grid2, row - 1, col, visited)
        self.dfs(grid1, grid2, row, col + 1, visited)
        self.dfs(grid1, grid2, row, col - 1, visited)

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        self.m, self.n, ans, visited = len(grid1), len(grid1[0]), 0, set()

        for i in range(self.m):
            for j in range(self.n):
                if (i, j) not in visited and grid2[i][j] == 1:
                    self.subIsland = True
                    self.dfs(grid1, grid2, i, j, visited)
                    if self.subIsland:
                        print(i, j)
                        ans += 1

        return ans
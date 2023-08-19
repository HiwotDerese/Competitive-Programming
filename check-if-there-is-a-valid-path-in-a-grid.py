class Solution:

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return 

        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        if self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x

        else:
            self.parent[root_x] = root_y
            
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        self.parent = {}
        self.rank = {}
        
        for row in range(m):
            for col in range(n):
                self.parent[(row, col)] = (row, col)
                self.rank[(row, col)] = 0

        directions = [(0, 1), (1, 0)]
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n

        possible_down = {1: [], 2: [2,5,6], 3: [2,5,6], 4: [2,5,6], 5:[], 6:[]}
        possible_right = {1: [1,3,5], 2: [], 3: [], 4: [1,3, 5], 5:[], 6:[1,3,5]}

        for row in range(m):
            for col in range(n):
                street = grid[row][col]
                
                for dx, dy in directions:
                    new_row = row + dx
                    new_col = col + dy

                    if inbound(new_row, new_col):
                        if dx == 1:
                            if grid[new_row][new_col] in possible_down[street]:
                                self.union((row, col), (new_row, new_col))
                        else:
                            if grid[new_row][new_col] in possible_right[street]:
                                self.union((row, col), (new_row, new_col))

        start_root = self.find((0, 0))
        end_root = self.find((m - 1, n - 1))

        if self.parent[start_root] == self.parent[end_root]:
            return True

        return False
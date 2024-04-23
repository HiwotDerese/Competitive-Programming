class Solution:
    def  dfs(self, row, col, board, visited):
        if (row, col) in visited or min(row, col) < 0 or row >= self.m or col >= self.n or board[row][col] == "X" :
            return
        
        # print(board)
        board[row][col] = "c"
        visited.add((row, col))
        self.dfs(row + 1, col, board, visited)
        self.dfs(row - 1, col, board, visited)
        self.dfs(row, col + 1, board, visited)
        self.dfs(row, col - 1, board, visited)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        self.m, self.n, visited = len(board), len(board[0]), set()

        for row in range(self.m):
            for col in range(self.n):

                if (row, col) not in visited:
                    if board[row][col] == "O" and (row == 0 or row == self.m - 1 or col == 0 or col == self.n - 1):
                        print(row, col)
                        self.dfs(row, col, board, visited)

        # print(board)

        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == "O":
                    board[row][col] = "X"


        for row in range(self.m):
            for col in range(self.n):
                if board[row][col] == "c":
                    board[row][col] = "O"


        return board
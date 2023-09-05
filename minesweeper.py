class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:

        if board[click[0]][click[1]] == "M":
            board[click[0]][click[1]] = "X"
            return board

        m, n = len(board), len(board[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, -1), (1, 1)]
        visited = set([(click[0], click[1])])

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n


        def dfs(row, col):

            found, count, valids = False, 0, []
            for dx, dy in directions:
                newx = row + dx
                newy = col + dy

                if inbound(newx, newy):
                    valids.append((newx, newy))
                    if board[newx][newy] == "M":
                        found = True
                        count += 1

            if found:
                board[row][col] = str(count)
                return board

            board[row][col] = "B"

            for newx, newy in valids:
                if (newx, newy) not in visited:
                    visited.add((newx, newy))
                    dfs(newx, newy)

            return board

        return dfs(click[0], click[1])
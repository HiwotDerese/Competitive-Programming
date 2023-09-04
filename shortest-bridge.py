class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:

        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n

        def dfs(row, col):
            if inbound(row, col) and grid[row][col] == 1:
                grid[row][col] = 2
                queue.append((row, col))
                for dx, dy in directions:
                    newx = row + dx
                    newy = col + dy
                    dfs(newx, newy)

        queue = deque([])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n, found = len(grid), False

        for row in range(n):
            for col in range(n):
                if grid[row][col] == 1:
                    dfs(row, col)
                    found = True
                    break
            if found:
                break

        ans = 1  
        while queue:
            leng = len(queue)
            for idx in range(leng):
                x, y = queue.popleft()
                
                for dx, dy in directions:
                    newx = x + dx
                    newy = y + dy

                    if inbound(newx, newy):
                        if grid[newx][newy] == 1:
                            return ans - 1
                        elif grid[newx][newy] == 0:
                            grid[newx][newy] = 2
                            queue.append((newx, newy))

            ans += 1

        return ans - 1
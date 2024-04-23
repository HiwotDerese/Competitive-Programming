class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
            
        n = len(grid)
        visited = set((0, 0))
        visited.add((0, 0))
        ans = 1


        directions = [(1, 0), (0, 1), (0, -1), (-1, 0),
                        (1, 1), (1, -1), (-1, -1), (-1, 1)]

        in_bound = lambda row, col : 0 <= row < n and 0 <= col < n

        queue = deque([(0, 0)])
        while queue:
            leng = len(queue)

            for i in range(leng):
                row, col = queue.popleft()

                if row == n - 1 and col == n - 1:
                    return ans

                for dx, dy in directions:
                    new_x = row + dx
                    new_y = col + dy

                    if in_bound(new_x, new_y) and (new_x, new_y) not in visited and\
                        grid[new_x][new_y] == 0:
                        queue.append((new_x, new_y))
                        visited.add((new_x, new_y))

            ans += 1

        return -1
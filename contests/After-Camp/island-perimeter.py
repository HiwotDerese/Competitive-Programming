class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n, m, ans = len(grid), len(grid[0]), 0
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m

        for row in range(n):
            for col in range(m):
                if grid[row][col] == 1:
                    for dx, dy in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
                        new_x, new_y = row + dx, col + dy
                        if not inbound(new_x, new_y):
                            ans += 1
                            continue
                        
                        if grid[new_x][new_y] == 1:
                            continue

                        ans += 1

        return ans

        
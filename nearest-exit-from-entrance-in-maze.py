class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        directions = [(0,0), (0, 1), (1, 0), (-1, 0), (0, -1)]
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n

        visited = set((entrance[0], entrance[1]))
        queue = deque([(entrance[0], entrance[1])])
        ans = 0

        while queue:
            curr_level = len(queue)

            for _ in range(curr_level):
                row, col = queue.popleft()

                if (row, col) != (entrance[0], entrance[1]) and (row == 0 or col == 0 or row == m - 1 or col == n - 1):
                    print((row, col), (entrance[0], entrance[1]) )
                    return ans
                
                for dx, dy in directions:
                    new_x = row + dx
                    new_y = col + dy

                    if inbound(new_x, new_y) and (new_x, new_y) not in visited and\
                        maze[new_x][new_y] == ".":
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
            ans += 1

        return -1
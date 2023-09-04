class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        
        visited = defaultdict(set)
        
        all_keys = 0
        for i in range(m):
            for j in range(n):
                cell = grid[i][j]

                if cell.islower():
                    all_keys += (1 << (ord(cell) - ord('a')))

                if cell == "@":
                    start_row, start_col = i, j
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue.append((start_row, start_col, 0, 0))
        visited[0].add((start_row, start_col))
        
        while queue:
            row, col, keys, moves = queue.popleft()
            for dx, dy in directions:
                newx, newy = row + dx, col + dy
                
                if 0 <= newx < m and 0 <= newy < n and grid[newx][newy] != '#':
                    cell = grid[newx][newy]
                    
                    if cell.islower() and not ((1 << (ord(cell) - ord('a'))) & keys):
                        new_keys = (keys | (1 << (ord(cell) - ord('a'))))

                        if new_keys == all_keys:
                            return moves + 1

                        visited[new_keys].add((newx, newy))
                        queue.append((newx, newy, new_keys, moves + 1))
                      
                    elif cell.isupper() and not (keys & (1 << (ord(cell) - ord('A')))):
                        continue
                        
                    elif (newx, newy) not in visited[keys]:
                        visited[keys].add((newx, newy))
                        queue.append((newx, newy, keys, moves + 1))
            
        return -1
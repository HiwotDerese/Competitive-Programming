class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = mat
        m,n = len(mat), len(mat[0])
        visited = set()
        queue = deque()
        for row in range(m):
            arr = []
            for col in range(n):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col))
                    
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        inbound = lambda row, col: 0 <= row < m and 0 <= col < n
        distance = 0
        while queue:
            distance += 1
            level_len = len(queue)

            for _ in range(level_len):
                row, col = queue.popleft()

                for dx, dy in directions:
                    new_x = row + dx
                    new_y = col + dy
                    if inbound(new_x, new_y) and (new_x, new_y) not in visited:
                        # print(ans, new_x, new_y)
                        visited.add((new_x, new_y))
                        queue.append((new_x, new_y))
                        ans[new_x][new_y] = distance

        return ans
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        n, m = len(dungeon), len(dungeon[0])
        directions = [(0, 1), (1, 0)]
        inbound = lambda x, y: 0 <= x < n and 0 <= y < m

        dp = [[-1] * m for i in range(n)] 
        min_ = [inf]

        def dfs(row, col):
            if row == n - 1 and col == m - 1:
                return max(1, 1 - dungeon[row][col])

            if dp[row][col] != -1:
                return dp[row][col]


            right = max(1, max(1, 1 - dungeon[row][col]))

            min_ = inf
            for dx, dy in directions:
                new_x, new_y = row + dx, col + dy

                if inbound(new_x, new_y):
                    curr = max(1, -dungeon[row][col] + dfs(new_x, new_y))
                    min_ = min(min_, curr)


            dp[row][col] = min_
            
            return dp[row][col]

        return dfs(0, 0)
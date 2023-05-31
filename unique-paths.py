class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = {}

        def dfs(row, col):

            if (row, col) in dp:
                return dp[(row, col)]
                
            if row == m or col == n:
                return 0

            if (row, col) == (m - 1, n - 1):
                return 1

            dp[(row, col)] = dfs(row + 1, col) + dfs(row, col + 1)

            return dp[(row, col)]

        
        return dfs(0, 0)
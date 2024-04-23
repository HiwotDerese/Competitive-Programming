class Solution:
    def minimumTotal(self, triangle):
        l = len(triangle)
        memo = [[-1 for i in range(len(triangle[j]))] for j in range(len(triangle))]
        #print(memo) 
        def dfs(row,idx):
            if row == l-1:
                return triangle[row][idx]

            if memo[row][idx] != -1:
                return memo[row][idx]

            memo[row][idx] = triangle[row][idx]+min(dfs(row+1,idx),dfs(row+1,idx+1))
            return memo[row][idx]

        ans = dfs(0,0)


        return ans




        # n, dp = len(triangle), {}

        # def dfs(row, col, sum_):
        #     if (row, sum_) in dp:
        #         return dp[(idx, sum_)]

        #     if row == n or col == len(triangle[row]):
        #         return 0

        #     path1 = dfs(row + 1, col, sum_ + triangle[row + 1][col])
        #     path2 = dfs(row + 1, col + 1, sum_ + triangle[row + 1][col + 1])

        #     dp[(row, sum_)] = triangles[row][col] + min(path1, path2)

        #     return dp[(row, sum_)]

        # return dfs(0, 0, 0)
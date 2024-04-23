class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        in_bound = lambda x, y:  x < n and x >= 0 and y < n and y >= 0

        for row in range(n - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                choice1, choice2, choice3 = inf, inf, inf

                if in_bound(row + 1, col - 1):
                    choice1 = matrix[row + 1][col - 1]

                if in_bound(row + 1, col):
                    choice2 = matrix[row + 1][col]

                if in_bound(row + 1, col + 1):
                    choice3 = matrix[row + 1][col + 1]
                
                min_ = min(choice1, choice2, choice3)

                if min_ != inf:
                    matrix[row][col] += min_

        return min(matrix[0])
                

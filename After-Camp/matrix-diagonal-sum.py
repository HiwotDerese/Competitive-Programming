class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        ans, n = 0, len(mat)
        row, col = 0, 0

        while row < n:
            ans += mat[row][col]
            row += 1
            col += 1

        row, col = 0, n - 1
        while row < n:
            ans += mat[row][col]
            row += 1
            col -= 1

        if n % 2 != 0:
            idx = n // 2
            ans -= mat[idx][idx]

        return ans

        
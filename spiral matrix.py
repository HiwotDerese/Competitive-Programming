class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        n = len(matrix[0])
        n2 = len(matrix)
        up = 0
        down = n2-1
        right = n-1
        left = 0
        dxn = 0
        while(up <= down and left <= right):
            if dxn == 0:
                for i in range(left,right+1,1):
                    ans.append(matrix[up][i])
                up +=1
            elif dxn == 1:
                for i in range(up,down+1,1):
                    ans.append(matrix[i][right])
                right -=1
            elif dxn == 2:
                for i in range(right,left-1,-1):
                    ans.append(matrix[down][i])
                down -=1
            elif dxn == 3:
                for i in range(down,up-1,-1):
                    ans.append(matrix[i][left])
                left +=1
            dxn = (dxn + 1)% 4
        return ans
            
                